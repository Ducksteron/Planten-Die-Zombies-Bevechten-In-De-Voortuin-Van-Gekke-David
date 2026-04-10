from classes import projectile_class
from classes import renderable_object_class
from managers import object_manager


class Plant(renderable_object_class.RenderableObject):
    def __init__(self: Plant,image_path: str, pos:dict[str,int]):
        super().__init__(image_path, pos)
        # self.hitbox = (self.x + 17, self.y + 11, 29, 52)
    firerate: float = 1 #rounds per second


   
    def process(self: Plant, delta_time: float) -> None:
        super().process(delta_time)
        
    _waited_time: float = 0
    def handle_shooting(self: Plant, delta_time: float) -> projectile_class.Projectile:
        self._waited_time +=  delta_time
        if delta_time == 0:
            return self.get_null_projectile()
        
        
        if self._waited_time >= self.firerate:
            self._waited_time = 0
            return self.shoot(projectile_class.Projectile("images/misc/goosington.png", self.pos))
            
        else:
            return self.get_null_projectile()
    
    def get_null_projectile(self: Plant) -> projectile_class.Projectile:
        null_projectile = projectile_class.Projectile("images/misc/goosington.png", self.pos)
        null_projectile.is_null = True
        return null_projectile

    def shoot(self: Plant, projectile: projectile_class.Projectile) -> projectile_class.Projectile:
        return projectile
    

