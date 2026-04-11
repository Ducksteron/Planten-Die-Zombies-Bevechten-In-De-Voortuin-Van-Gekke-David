from classes.game_object_class import GameObject
from classes.projectile_class import Projectile
from managers import render_image_wrapper as renderer
from classes import renderable_object_class as ROC
import pygame


class Zombie(ROC.RenderableObject):
    def __init__(self: Zombie,image_path: str, pos:dict[str,int]):
        super().__init__(image_path, pos)
        self.collision_layer = 1

    health: int = 100
   
    def process(self: Zombie, delta_time: float) -> None:
        super().process(delta_time)
    
        self.pos = {"x": self.pos["x"] - 100 * delta_time, "y": self.pos["y"]}
        if self.pos["x"] < -100:
            self.is_null = True
    
    def draw(self: Zombie, screen, use_given_trans_dict: bool = False, given_trans_dict: dict = {}):
        super().draw(screen, use_given_trans_dict, given_trans_dict)
    
    def damage_self(self: Zombie, damage:int) -> None:
        self.health -= damage
        if self.health <= 0:
            self.is_null = True
        

