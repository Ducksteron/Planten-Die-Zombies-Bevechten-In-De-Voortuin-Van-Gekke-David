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

        if is_first_frame:
            all_objects.append(planter.plant_plant({"x":1,"y":1}, "test"))
            all_objects.append(planter.plant_plant({"x":2,"y":2}, "test"))
            all_objects.append(planter.plant_plant({"x":3,"y":3}, "test"))
            all_objects.append(planter.plant_plant({"x":4,"y":4}, "test"))
            
            # all_objects.append(planter.plant_plant({"x":-1,"y":0}, "test"))
            # all_objects.append(planter.plant_plant({"x":999,"y":0}, "test"))
            # all_objects.append(planter.plant_plant({"x":0,"y":-1}, "test"))
            # all_objects.append(planter.plant_plant({"x":8,"y":987896}, "test"))
            


        object_manager.handle_shooting(all_objects, dt)

        #removes all null instances from all objects
        all_objects = object_manager.remove_null_instances(all_objects)
        #call process for all objects
        object_manager.process_objects(all_objects, dt)
        #call draw for all objects
        object_manager.draw_objects(all_objects, screen)
        


        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 120
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(120) / 1000

        is_first_frame = False

    pygame.quit()


def render_background(screen):
    renderer.render(screen,"images/backgrounds/cropped frontyard.png", {"x":0,"y":0})