import pygame
from managers import render_image_wrapper as renderer
from managers import plant_plant as planter
from managers import object_manager
from classes import game_object_class
from classes import plant_class


def start_game():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((843, 600))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    all_objects: list[game_object_class.GameObject] = []
    is_first_frame: bool = True

    horse_trans_dict = renderer.scale_by_trans_dict({},0.1)


    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        render_background(screen)

        # ps_trans_dict = renderer.scale_by_trans_dict({}, 0.25)
        # renderer.render(screen,"images/plants/peashooter.png", 50,50, ps_trans_dict)

        # planter.plant_plant(screen,{"x":0,"y":0}, "hello")
        # planter.plant_plant(screen,{"x":8,"y":4}, "hello")
        # planter.plant_plant(screen,{"x":8,"y":0}, "hello")
        # planter.plant_plant(screen,{"x":0,"y":4}, "hello")

        # planter.plant_plant(screen,{"x":1,"y":1}, "hello")
        # planter.plant_plant(screen,{"x":3,"y":2}, "hello")


        if is_first_frame:
            new_plant = plant_class.Plant("images/misc/german_horse.png", {"x":200,"y": 200})
            new_plant.trans_dict = horse_trans_dict
            all_objects.append(new_plant)
            
        horse_trans_dict = renderer.rotate_trans_dict(horse_trans_dict, 20 *dt)
        # plant_class.Plant.draw(new_plant, screen, True, horse_trans_dict)


        #call process for all objects
        object_manager.process_objects(all_objects, dt)
        #call draw for all objects
        object_manager.draw_objects(all_objects, screen)

        is_first_frame = False


        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 120
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(120) / 1000
        print(dt)

    pygame.quit()


def render_background(screen):
    renderer.render(screen,"images/backgrounds/cropped frontyard.png", {"x":0,"y":0})