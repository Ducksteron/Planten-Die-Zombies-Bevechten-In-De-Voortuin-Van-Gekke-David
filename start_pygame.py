import pygame
from managers import render_image_wrapper as renderer
from managers import plant_plant as planter
from managers import zombie_spawner
from managers import object_manager
from managers import input_manager
from classes import game_object_class


def start_game():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((843, 600))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    all_objects: list[game_object_class.GameObject] = []
    board: planter.Board = planter.Board(8, 4)
    background_image = pygame.image.load("images/backgrounds/cropped frontyard.png")
    is_first_frame: bool = True


    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        render_background(screen, background_image)

        if is_first_frame:
            all_objects.append(planter.plant_plant({"x":1,"y":1}, "peashooter", board))
            all_objects.append(planter.plant_plant({"x":1,"y":2}, "peashooter", board))
            all_objects.append(planter.plant_plant({"x":1,"y":3}, "repeater", board))
            all_objects.append(planter.plant_plant({"x":1,"y":3}, "repeater", board))
            planter.remove_plant({"x":1,"y":3}, board)
            planter.remove_plant({"x":5,"y":2}, board)
            
            new_zombies: list = []
            new_zombies.append(zombie_spawner.spwn_zombie(0, "basic"))
            new_zombies.append(zombie_spawner.spwn_zombie(1, "basic"))
            new_zombies.append(zombie_spawner.spwn_zombie(2, "conehead"))
            new_zombies.append(zombie_spawner.spwn_zombie(3, "conehead"))
            new_zombies.append(zombie_spawner.spwn_zombie(4, "basic"))
            new_zombies.append(zombie_spawner.spwn_zombie(5, "basic"))

            for new_zombie_object_list in new_zombies:
                for new_zombie_object in new_zombie_object_list:
                    all_objects.append(new_zombie_object)

        
        all_objects.append( planter.handle_planting(board, input_manager.handle_input(screen)))
        # print(input_manager.handle_input(screen))


        # for event in pygame.event.get():
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         print("jorkjerk")
        # print(pygame.mouse.get_pressed())
        # if pygame.mouse.get_pressed()[0]:
            # print("sexsox")


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


        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 120
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(120) / 1000

        is_first_frame = False

        # print(1/dt)

    pygame.quit()


def render_background(screen, background_image):
    renderer.render(screen,background_image, {"x":0,"y":0})