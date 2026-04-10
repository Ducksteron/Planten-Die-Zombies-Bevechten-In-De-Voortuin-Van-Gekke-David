from managers import render_image_wrapper as renderer
from classes import plant_class


def plant_plant(position: dict[str,int], type: str) -> plant_class.Plant:
    if position["x"] > 8 or position["x"] < 0 or position["y"] > 4 or position["y"] < 0:
        print("plant_plant.py: given position is not valid! return null plant.")
        new_plant = plant_class.Plant("images/plants/peashooter.png", {"x": 67, "y":67})
        new_plant.is_null = True
        return new_plant

    pixel_position = get_spawn_pos(position, {"x":65,"y":80}, {"x":82,"y":100}, {"x":9,"y":5})
    
    new_plant = plant_class.Plant("images/plants/peashooter.png", pixel_position)
    ps_trans_dict = renderer.scale_by_trans_dict({}, 0.166666666)
    new_plant.trans_dict = ps_trans_dict

    return new_plant


def get_spawn_pos(looking_for_pos: dict[str,int], start_pos: dict[str,int], offsets: dict[str,int], total_positions: dict[str,int]) -> dict[str,int]:
    return_x_pos:int = start_pos["x"] + (offsets["x"] * looking_for_pos["x"])
    return_y_pos:int = start_pos["y"] + (offsets["y"] * looking_for_pos["y"])
    return {"x": return_x_pos, "y": return_y_pos}

