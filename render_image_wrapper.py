import pygame

def render(screen, path):
    image = pygame.image.load(path)
    imagerect = image.get_rect()

    screen.blit(image, imagerect)