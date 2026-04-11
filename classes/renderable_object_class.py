from classes import game_object_class
from managers import render_image_wrapper as renderer
import pygame

class RenderableObject(game_object_class.GameObject):
    def __init__(self: RenderableObject,image_path: str, pos:dict[str,int]) -> None:
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.pos = pos
        self.trans_dict = {}
    
    def draw(self,screen, use_given_trans_dict:bool = False, given_trans_dict: dict[str,dict] = {}) -> None:
        if use_given_trans_dict:
            self.trans_dict = given_trans_dict
        image = renderer.render(screen,self.image,self.pos,self.trans_dict)
    
    def process(self: RenderableObject, delta_time: float) -> None:
        super().process(delta_time)