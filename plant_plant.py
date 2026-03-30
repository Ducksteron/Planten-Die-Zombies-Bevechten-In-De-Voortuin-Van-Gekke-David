import render_image_wrapper as renderer
import pygame


def plant_plant(screen, position: dict[str,int], type: str):
    pixel_position = get_spawn_pos(position, {"x":65,"y":80}, {"x":82,"y":100}, {"x":9,"y":5})
    
    ps_trans_dict = renderer.scale_by_trans_dict({}, 0.166666666)
    renderer.render(screen,"images/plants/peashooter.png", pixel_position, ps_trans_dict)


def get_spawn_pos(looking_for_pos: dict[str,int], start_pos: dict[str,int], offsets: dict[str,int], total_positions: dict[str,int]) -> dict[str,int]:
    return_x_pos:int = start_pos["x"] + (offsets["x"] * looking_for_pos["x"])
    return_y_pos:int = start_pos["y"] + (offsets["y"] * looking_for_pos["y"])
    return {"x": return_x_pos, "y": return_y_pos}





# def get_all_spawn_pos(start_pos: dict[str,int], offsets: dict[str,int], pos_amt: dict[str,int]) -> dict[int, dict[int, dict[str,int]]]:
#     all_positions: dict[int, dict[int, dict[str,int]]] = {}
#     for x_pos_index in range(pos_amt["x"]):
#         all_positions[x_pos_index] = {0 :{"x": 0, "y":0}}
    
#     for y_pos_index in range(pos_amt["y"]):
#         pass


#     return {0:{0:{"x":0,"y":0}}}