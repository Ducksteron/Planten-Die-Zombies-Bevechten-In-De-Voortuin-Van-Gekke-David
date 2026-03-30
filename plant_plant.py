import render_image_wrapper as renderer



def get_spawn_pos(looking_for_pos: dict[str,int], start_pos: dict[str,int], offsets: dict[str,int], total_positions: dict[str,int]) -> dict[str,int]:
    return_x_pos:int = start_pos["x"] + (offsets["x"] * looking_for_pos["x"])
    return_y_pos:int = start_pos["y"] + (offsets["x"] * looking_for_pos["x"])
    return {"x": return_x_pos, "y": return_y_pos}





# def get_all_spawn_pos(start_pos: dict[str,int], offsets: dict[str,int], pos_amt: dict[str,int]) -> dict[int, dict[int, dict[str,int]]]:
#     all_positions: dict[int, dict[int, dict[str,int]]] = {}
#     for x_pos_index in range(pos_amt["x"]):
#         all_positions[x_pos_index] = {0 :{"x": 0, "y":0}}
    
#     for y_pos_index in range(pos_amt["y"]):
#         pass


#     return {0:{0:{"x":0,"y":0}}}