from classes.game_object_class import GameObject 
from classes.zombie_class import Zombie


def is_game_ended(all_objects: list[GameObject]) -> bool:
    for object in all_objects:
        if not issubclass(type(object), Zombie):
            continue
        
        zombie: Zombie = object #type: ignore
        if zombie.pos["x"] < - 100:
            return True
    
    return False