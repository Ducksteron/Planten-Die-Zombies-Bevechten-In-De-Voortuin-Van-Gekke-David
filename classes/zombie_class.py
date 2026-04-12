from classes.game_object_class import GameObject
from classes.projectile_class import Projectile
from classes.renderable_object_class import RenderableObject
from classes.plant_class import Plant
from managers import render_image_wrapper as renderer

import pygame


class Zombie(RenderableObject):
    def __init__(self: Zombie,image_path: str, pos:dict[str,int], max_health):
        super().__init__(image_path, pos)
        self.collision_layer = 1
        self.current_health = max_health
        self.max_health = max_health

    current_health:int
    max_health:int 
    is_eating: bool = False
    eating_plant: Plant
    damage_per_second: int
    child_plant_detector: PlantDetector
    waited_time:float = 0.0

    def get_child_plant_detector(self: Zombie) -> PlantDetector:
        self.child_plant_detector = PlantDetector("images/misc/german_horse.png", self.pos, self)
        return self.child_plant_detector



    def process(self: Zombie, delta_time: float) -> None:
        super().process(delta_time)

        if not self.is_eating:
            self.pos = {"x": self.pos["x"] - 100 * delta_time, "y": self.pos["y"]}
        
        if self.pos["x"] < -100:
            self.is_null = True
    
    def draw(self: Zombie, screen, use_given_trans_dict: bool = False, given_trans_dict: dict = {}):
        super().draw(screen, use_given_trans_dict, given_trans_dict)
    
    def damage_self(self: Zombie, damage:int) -> None:
        self.current_health -= damage
        if self.current_health <= 0:
            self.is_null = True
            self.child_plant_detector.is_null = True
    
    waited_time: float
    def handle_eating(self: Zombie, delta_time: float) -> None:
        if not self.is_eating:
            return
        self.waited_time += delta_time
        if self.waited_time >= 1:
            self.eating_plant.damage_self(int(self.damage_per_second * self.waited_time)) #type: ignore
            self.waited_time = 0
        if self.eating_plant.current_health <= 0:
            self.is_eating = False

        
class PlantDetector(RenderableObject):
    def __init__(self: PlantDetector,image_path: str, pos:dict[str,int], parent_zombie: Zombie):
        super().__init__(image_path, pos)
        self.parent_zombie = parent_zombie
        self.show_col_box = False
        self.use_default_col_box = False
        self.visible = False
        

    parent_zombie: Zombie

    def process(self: PlantDetector, delta_time: float) -> None:
        super().process(delta_time)

        self.pos = self.parent_zombie.pos
        if self.pos["x"] < -100:
            self.is_null = True
    
    
    def draw(self: PlantDetector,screen, use_given_trans_dict:bool = False, given_trans_dict: dict[str,dict] = {}):
        
        super().draw(screen, use_given_trans_dict, given_trans_dict)
        
        self.collision_layer = 2
        #+40 on y to not get top plants
        self.collision_rect = pygame.Rect(self.pos["x"], self.pos["y"] + 40, self.parent_zombie.collision_rect.w/2, self.parent_zombie.collision_rect.h/2)

    def on_collision(self:PlantDetector, collision_body: GameObject) -> None:
        self.on_plant_collision(collision_body) #type: ignore


    def on_plant_collision(self: PlantDetector, plant: Plant):
        self.parent_zombie.is_eating = True
        self.parent_zombie.eating_plant = plant
        


class BasicZombie(Zombie):
    def __init__(self: BasicZombie, image_path: str, pos: dict[str, int]):
        self.max_health = 100
        super().__init__("images/zombies/zombie.png", pos, max_health = self.max_health)
        self.damage_per_second = 50
        self.trans_dict = renderer.scale_by_trans_dict(self.trans_dict, 0.05)


class Conehead(Zombie):
    def __init__(self: Conehead, image_path: str, pos: dict[str, int]):
        self.max_health = 400
        super().__init__("images/zombies/conehead.webp", pos, max_health = self.max_health)
        self.damage_per_second = 50
        self.trans_dict = renderer.scale_by_trans_dict(self.trans_dict, 0.2)
