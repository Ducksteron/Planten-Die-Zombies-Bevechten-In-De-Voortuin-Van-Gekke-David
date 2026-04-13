from managers import render_image_wrapper as renderer
from classes import renderable_object_class
from classes.game_object_class import GameObject

class Projectile(renderable_object_class.RenderableObject):
    damage: int = 50

    def __init__(self: Projectile, image_path: str, pos:dict[str,int]) -> None:
        super().__init__(image_path, pos)
        self.collision_layer = 1

    def draw(self: Projectile,screen, use_given_trans_dict:bool = False, given_trans_dict: dict[str,dict] = {}) -> None:
        super().draw(screen, use_given_trans_dict, given_trans_dict)
    
    def move(self: Projectile, delta_time: float) -> None:
        self.pos = {"x": self.pos["x"] + 100 * delta_time, "y": self.pos["y"]}
        if self.pos["x"] > 900:
            self.is_null = True

    def process(self: Projectile, delta_time: float) -> None:
        super().process(delta_time)
        self.move(delta_time)
    
    def on_collision(self: Projectile, collision_body: GameObject) -> None:
        super().on_collision(collision_body)
        if self.is_null:
            return

        if issubclass(type(collision_body), GameObject) and not issubclass(type(collision_body), Projectile):
            self.on_zombie_collision(collision_body) #type: ignore
    
    def on_zombie_collision(self: Projectile, zombie: GameObject) -> None:
        zombie.damage_self(self.damage) #type: ignore
        self.is_null = True