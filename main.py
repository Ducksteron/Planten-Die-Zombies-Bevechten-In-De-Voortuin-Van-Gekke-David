import pygame
from managers import render_image_wrapper as renderer
from managers import plant_plant as planter
from managers import zombie_spawner
from managers import object_manager
from managers import input_manager
from managers import sun_manager
from managers import text_renderer
from managers import game_ender
from managers import sql_wrapper
from managers import write_box
from managers import final_stats_displayer
from managers import logger
from managers import log_printer
from classes import game_object_class
from classes.game_stats import GameStats


def main():
    # pygame setup
    pygame.init()
    
    
    background_image = pygame.image.load("images/backgrounds/cropped frontyard.png")
    screen = pygame.display.set_mode((843, 600))
    loaded_font = pygame.font.Font('freesansbold.ttf', 32)
    
    clock = pygame.time.Clock()
    running: bool = True
    died: bool = False
    dt: float = 0
    name_string: str = ""
    logged_start: bool = False
    player_id:int = -1
    game_id:int = -1

    sunwallet: sun_manager.SunWallet = sun_manager.SunWallet()
    elapsed_time: float = 0.0
    all_objects: list[game_object_class.GameObject] = []
    board: planter.Board = planter.Board(8, 4)
    game_stats: GameStats = GameStats()
    


    while running: #main loop
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        input_events = pygame.event.get()
        for event in input_events:
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        if game_stats.name == "":
            name_string = get_name(name_string,input_events,game_stats,loaded_font,screen)
            dt = clock.tick(120) / 1000
            pygame.display.flip()
            continue
        elif not logged_start:
            logger.log_action("start", game_stats.name)
            logged_start = True


        render_background(screen, background_image)

        
        all_objects.append( planter.handle_planting(board, input_manager.handle_input(screen), sunwallet, game_stats))
        all_objects = zombie_spawner.handle_zombie_spawning(all_objects, elapsed_time, game_stats)
        sun_manager.increase_sun(dt, sunwallet)
        text_renderer.render_text(screen, ("sun = " + str(int(sunwallet.amount_of_sun))), loaded_font, {"x":0,"y":0}, pygame.Color(0,0,0,255))
       

        #removes all null instances from all objects
        all_objects = object_manager.remove_null_instances(all_objects, board)

        object_manager.handle_shooting(all_objects, dt)
        object_manager.handle_zombies_eating(all_objects,dt)

        object_manager.handle_collision(all_objects)
        #call process for all objects
        object_manager.process_objects(all_objects, dt)
        #call draw for all objects
        object_manager.draw_objects(all_objects, screen)
        
        #removes all null instances from all objects
        all_objects = object_manager.remove_null_instances(all_objects, board)

        
        game_stats.sun_collected = sunwallet.total_sun_gotten
        game_stats.time_survived = elapsed_time


        if game_ender.is_game_ended(all_objects): # zombie got past bariers
            running = False
            died = True


        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 120
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(120) / 1000

        elapsed_time += dt


    all_objects = []
    is_displaying_leaderboard: bool = False

    
    displaying_end_screen: bool = True
    while displaying_end_screen:
        input_events = pygame.event.get()
        if not died:
            break
        for event in input_events:
            if event.type == pygame.QUIT:
                displaying_end_screen = False

        screen.fill("black")
        text_renderer.render_text(screen,"The zombies ate your brains!", loaded_font, {"x": 100, "y": 100}, pygame.Color(255,255,255,255))
        
        if game_stats.name != "" and game_id == -1:
            new_game_ids = sql_wrapper.insert_stats(game_stats)
            player_id = new_game_ids["player id"]
            game_id = new_game_ids["game id"]
            
        game_data_dict = sql_wrapper.get_stats_from_db(player_id, game_id)
        is_displaying_leaderboard = final_stats_displayer.show_final_stats(screen, loaded_font, game_data_dict, input_events, is_displaying_leaderboard, sql_wrapper.get_leaderboard(5))

        log_printer.handle_log_printing(input_events)



        pygame.display.flip()
        dt = clock.tick(10) / 1000


    logger.log_action("end", game_stats.name)
    pygame.quit()


def get_name(name_string, input_events, game_stats, loaded_font, screen) -> str:
    name_string = write_box.handle_writing("Your name = ", name_string, input_events, game_stats)
    text_renderer.render_text(screen,name_string, loaded_font, {"x": 100, "y": 150}, pygame.Color(255,255,255,255))
    return name_string

def render_background(screen, background_image):
    renderer.render(screen,background_image, {"x":0,"y":0})


if __name__ == "__main__":
    main()