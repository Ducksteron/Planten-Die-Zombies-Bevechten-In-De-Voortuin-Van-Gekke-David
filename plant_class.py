import render_image_wrapper as renderer
import pygame

class RenderableObject():
    def __init__(self: RenderableObject,image_path: str, pos:dict[str,int]) -> None:
        self.image_path = image_path
        self.pos = pos
        self.trans_dict = {}
    
    def draw(self,screen, use_given_trans_dict:bool = False, given_trans_dict: dict[str,dict] = {}) -> None:
        if use_given_trans_dict:
            self.trans_dict = given_trans_dict
        image = renderer.render(screen,self.image_path,self.pos,self.trans_dict)
    
    def process(self: RenderableObject, screen, delta_time: float) -> None:
        self.draw(screen)

        


class Plant(RenderableObject):
    def __init__(self: Plant,image_path: str, pos:dict[str,int]):
        super().__init__(image_path, pos)
        # self.hitbox = (self.x + 17, self.y + 11, 29, 52)
    
    def process(self: Plant, screen, delta_time: float) -> None:
        super().process(screen, delta_time)
        self.draw(screen)
    
    def shoot(self: Plant, projectile: Projectile, screen, delta_time: float) -> Projectile:
        return projectile


class Projectile(RenderableObject):
    def __init__(self: Projectile, image_path: str, pos:dict[str,int]) -> None:
        super().__init__(image_path, pos)

    def draw(self: Projectile,screen, use_given_trans_dict:bool = False, given_trans_dict: dict[str,dict] = {}) -> None:
        super().draw(screen, use_given_trans_dict, given_trans_dict)
    
    def move(self: Projectile, delta_time: float) -> None:
        self.pos = {"x": self.pos["x"] + 10 * delta_time, "y": self.pos["y"]}
    
    def process(self: Projectile, screen, delta_time: float) -> None:
        super().process(screen, delta_time)
        self.move(delta_time)
        self.draw(screen)
