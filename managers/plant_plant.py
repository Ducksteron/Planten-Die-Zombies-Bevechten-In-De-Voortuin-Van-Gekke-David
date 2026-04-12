from managers import render_image_wrapper as renderer
from classes import plant_class


def plant_plant(position: dict[str,int], type: str) -> plant_class.Plant:
    if position["x"] > 8 or position["x"] < 0 or position["y"] > 4 or position["y"] < 0:
        print("plant_plant.py: given position is not valid! return null plant.")
        return get_null_plant()

    pixel_position = get_spawn_pos(position, {"x":65,"y":80}, {"x":82,"y":100}, {"x":9,"y":5})
    
    new_plant: plant_class.Plant
    if type == "peashooter":
        new_plant = plant_class.Peashooter("", pixel_position)
    elif type == "repeater":
        new_plant = plant_class.Repeater("", pixel_position)
    else:
        print("plant_plant.py: given type not recognized! returning null plant.")
        new_plant = get_null_plant()

    return new_plant

def get_null_plant() -> plant_class.Plant:
    new_plant = plant_class.Plant("images/plants/peashooter.png", {"x": 67, "y":67}, 67)
    new_plant.is_null = True
    return new_plant



def get_spawn_pos(looking_for_pos: dict[str,int], start_pos: dict[str,int], offsets: dict[str,int], total_positions: dict[str,int]) -> dict[str,int]:
    return_x_pos:int = start_pos["x"] + (offsets["x"] * looking_for_pos["x"])
    return_y_pos:int = start_pos["y"] + (offsets["y"] * looking_for_pos["y"])
    return {"x": return_x_pos, "y": return_y_pos}

