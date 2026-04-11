from classes.zombie_class import Zombie
from managers import render_image_wrapper as renderer


def spwn_zombie(lane:int, type: str) -> Zombie:
    if lane < 0 or lane > 4:
        print("plant_plant.py: given position is not valid! return null zombie.")
        new_zombie = Zombie("images/zombies/zombie.png", {"x":800,"y":120})
        new_zombie.is_null = True
        return new_zombie

    pixel_position = {"x": 800, "y": get_spawn_pos(lane, 80, 100)}
    
    new_zombie = Zombie("images/zombies/zombie.png", pixel_position)
    new_zombie.trans_dict = renderer.scale_by_trans_dict(new_zombie.trans_dict, 0.05)

    return new_zombie

def get_spawn_pos(looking_for_lane: int, start_y: int, offset: int) -> int:
    return start_y + (offset * looking_for_lane)