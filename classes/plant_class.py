from classes import projectile_class
from classes import renderable_object_class


class Plant(renderable_object_class.RenderableObject):
    def __init__(self: Plant,image_path: str, pos:dict[str,int]):
        super().__init__(image_path, pos)
        # self.hitbox = (self.x + 17, self.y + 11, 29, 52)
    
    def process(self: Plant, delta_time: float) -> None:
        super().process(delta_time)
    
    def shoot(self: Plant, projectile: projectile_class.Projectile, screen, delta_time: float) -> projectile_class.Projectile:
        return projectile

