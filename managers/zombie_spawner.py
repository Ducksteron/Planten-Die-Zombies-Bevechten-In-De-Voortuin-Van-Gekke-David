from classes import zombie_class
from managers import render_image_wrapper as renderer


def spwn_zombie(lane:int, type: str) -> list:
    if lane < 0 or lane > 4:
        print("plant_plant.py: given position is not valid! return null zombie.")
        null_zombie = get_null_zombie()
        return [null_zombie, null_zombie.get_child_plant_detector()]

    pixel_position = {"x": 800, "y": get_spawn_pos(lane, 60, 100)}
    
    new_zombie: zombie_class.Zombie
    if type == "basic":
        new_zombie = zombie_class.BasicZombie("", pixel_position)
    elif type == "conehead":
        new_zombie = zombie_class.Conehead("", pixel_position)
    else:
        print("zombie_spawner.py: given type not recognized! returning null zombie.")
        new_zombie = get_null_zombie()


    return [new_zombie, new_zombie.get_child_plant_detector()]

def get_null_zombie() -> zombie_class.Zombie:
    new_zombie = zombie_class.Zombie("images/zombies/zombie.png", {"x":800,"y":120}, 676767)
    new_zombie.is_null = True
    return new_zombie

def get_spawn_pos(looking_for_lane: int, start_y: int, offset: int) -> int:
    return start_y + (offset * looking_for_lane)