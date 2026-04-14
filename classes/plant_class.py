from classes import projectile_class
from classes import renderable_object_class
from classes.game_stats import GameStats
from managers import object_manager
from managers import render_image_wrapper as renderer

class Plant(renderable_object_class.RenderableObject):
    def __init__(self: Plant,image_path: str, pos:dict[str,int], game_stats : GameStats, max_health: int):
        super().__init__(image_path, pos)
        self.collision_layer = 2
        self.show_col_box = False
        self.max_health = max_health
        self.current_health = max_health
        self.game_stats = game_stats

    firerate: float = 1#seconds per round
    cost: int = 0
    max_health: int = 1
    current_health: int = 1
    projectile_spawn_offset: dict[str,int]
    projectile_image_path:str
    position: dict[str,int] = {}
    game_stats: GameStats

   
    def process(self: Plant, delta_time: float) -> None:
        super().process(delta_time)
        
    _waited_time: float = 0
    def handle_shooting(self: Plant, delta_time: float) -> projectile_class.Projectile:
        self._waited_time +=  delta_time
        if delta_time == 0:
            return self.get_null_projectile()
        
        
        if self._waited_time >= self.firerate: 
            self._waited_time = 0
            new_projectile: projectile_class.Projectile = projectile_class.Projectile("images/projectiles/pea.png", {"x": self.pos["x"] + self.projectile_spawn_offset["x"], "y": self.pos["y"] + self.projectile_spawn_offset["y"]})
            new_projectile.trans_dict = renderer.scale_by_trans_dict(new_projectile.trans_dict, 0.5)
            return self.shoot(new_projectile)
            
        else:
            return self.get_null_projectile()
    
    def get_null_projectile(self: Plant) -> projectile_class.Projectile:
        null_projectile = projectile_class.Projectile("images/misc/goosington.png", self.pos)
        null_projectile.is_null = True
        return null_projectile

    def shoot(self: Plant, projectile: projectile_class.Projectile) -> projectile_class.Projectile:
        return projectile
    
    def damage_self(self: Plant, damage: int):
        
        self.current_health -= damage
        self.current_health
        if self.current_health <= 0:
            self.die()
    
    def die(self: Plant):
        self.is_null = True
        self.collision_layer = -1
    
class Peashooter(Plant):
    def __init__(self: Peashooter,image_path: str, pos:dict[str,int], game_stats: GameStats):
        super().__init__( "images/plants/peashooter.png", pos,game_stats, max_health=100)
        self.firerate = 1
        self.cost = 100
        self.current_health = self.max_health
        self.projectile_spawn_offset = {"x":50,"y":10}
        self.projectile_image_path= "images/projectiles/pea.png"
        # self.image_path = "images/plants/peashooter.png"
        self.trans_dict = renderer.scale_by_trans_dict({}, 0.166666666)

        
        
        

class Repeater(Plant):
    def __init__(self: Repeater,image_path: str, pos:dict[str,int], game_stats: GameStats):
        super().__init__("images/plants/repeater.webp", pos,game_stats,  max_health=100)
        self.firerate = 0.5
        self.max_health = 100
        self.cost = 200
        self.current_health = self.max_health
        self.projectile_spawn_offset = {"x":50,"y":10}
        self.projectile_image_path= "images/projectiles/pea.png"
        # self.image_path = "images/plants/repeater.webp"
        self.trans_dict = renderer.scale_by_trans_dict({}, 0.0833333333333)

        
