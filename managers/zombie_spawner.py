from classes.game_object_class import GameObject
from classes import zombie_class
from classes.game_stats import GameStats
from managers import render_image_wrapper as renderer
import random


def handle_zombie_spawning(all_objects: list[GameObject], elapsed_time:float, game_stats: GameStats) -> list[GameObject]:
    difficulty:float = 100 #the higher, the easier 1000
    zombie_types: list[str] = ["basic", "conehead"] #ascending toughness
    
    threshold = pow((elapsed_time/difficulty), 2)
    
    
    
    if threshold > 1:
        threshold = 1
    

    zombie_list: list = []

    random_number = random.random()
    
    if random_number < threshold:
        zombie_type = zombie_types[int(threshold * random_number / (1/len(zombie_types)))]
        
        zombie_list = spawn_zombie(random.randint(0,4),zombie_type, game_stats)
    
    for zombie_item in zombie_list:
        all_objects.append(zombie_item)
    
    return all_objects



def spawn_zombie(lane:int, type: str, game_stats: GameStats) -> list:
    if lane < 0 or lane > 4:
        print("plant_plant.py: given position is not valid! return null zombie.")
        null_zombie = get_null_zombie()
        return [null_zombie, null_zombie.get_child_plant_detector()]

    pixel_position = {"x": 800, "y": get_spawn_pos(lane, 60, 100)}
    
    new_zombie: zombie_class.Zombie
    if type == "basic":
        new_zombie = zombie_class.BasicZombie(pixel_position, game_stats)
    elif type == "conehead":
        new_zombie = zombie_class.Conehead(pixel_position, game_stats)
    else:
        print("zombie_spawner.py: given type not recognized! returning null zombie.")
        new_zombie = get_null_zombie()


    return [new_zombie, new_zombie.get_child_plant_detector()]

def get_null_zombie() -> zombie_class.Zombie:
    new_zombie = zombie_class.Zombie("images/zombies/zombie.png", {"x":800,"y":120},GameStats(), 676767)
    new_zombie.is_null = True
    return new_zombie

def get_spawn_pos(looking_for_lane: int, start_y: int, offset: int) -> int:
    return start_y + (offset * looking_for_lane)