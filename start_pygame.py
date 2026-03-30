import pygame
import render_image_wrapper as renderer
import plant_plant as planter


def start_game():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((843, 600))
    clock = pygame.time.Clock()
    running = True
    dt = 0

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

        planter.plant_plant(screen,{"x":0,"y":0}, "hello")
        planter.plant_plant(screen,{"x":8,"y":4}, "hello")
        planter.plant_plant(screen,{"x":8,"y":0}, "hello")
        planter.plant_plant(screen,{"x":0,"y":4}, "hello")

        planter.plant_plant(screen,{"x":1,"y":1}, "hello")
        planter.plant_plant(screen,{"x":3,"y":2}, "hello")



        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()


def render_background(screen):
    renderer.render(screen,"images/backgrounds/cropped frontyard.png", 0, 0)