import pygame
from managers import render_image_wrapper as renderer

def render_text(screen,text:str,font: pygame.font.Font, pos:dict[str,int], color: pygame.Color) -> None:
    text_surface: pygame.Surface = font.render(text, True, color)
    renderer.render(screen, text_surface, pos)

    