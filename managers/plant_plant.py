from managers import render_image_wrapper as renderer
from classes import plant_class


def handle_planting(board: Board, input_dict:dict) -> plant_class.Plant:
    new_plant: plant_class.Plant = get_null_plant()

    if not input_dict["event_happened"]:
        return new_plant
    
    pos = input_dict["position"]
    if input_dict["event"] == "plant":
        return plant_plant(pos, input_dict["type"], board)
    elif input_dict["event"] == "remove":
        remove_plant(pos, board)
    
    return new_plant


def plant_plant(position: dict[str,int], type: str, board: Board) -> plant_class.Plant:
    if not is_in_range(position):
        print("plant_plant.py: given position is not valid! return null plant.")
        return get_null_plant()
    
    if is_square_occupied(board, position):
        print("plant_plant.py: given position is occupied! return null plant.")
        return get_null_plant()


    pixel_position = get_spawn_pos(position, {"x":65,"y":80}, {"x":82,"y":100}, {"x":9,"y":5})
    
    new_plant: plant_class.Plant
    if type == "peashooter":
        new_plant = plant_class.Peashooter("", pixel_position)
    elif type == "repeater":
        new_plant = plant_class.Repeater("", pixel_position)
    else:
        print("plant_plant.py: given type not recognized! returning null plant.")
        return get_null_plant()
    new_plant.position = position


    board.legal_moves[position["x"]][position["y"]] = False
    board.plants[position["x"]][position["y"]] = new_plant

    return new_plant

def remove_plant(position: dict[str,int], board: Board) -> None:
    if not is_in_range(position):
        print("plant_plant.py: trying to remove plant is out of range! returning.")
        return
    
    if not is_square_occupied(board, position):
        print("plant_plant.py: given position is not occupied, cant remove plant! returning.")
        return

    to_remove_plant: plant_class.Plant = board.plants[position["x"]][position["y"]] #type: ignore
    to_remove_plant.is_null = True

    board.legal_moves[position["x"]][position["y"]] = True
    board.plants[position["x"]][position["y"]] = None
    




def get_null_plant() -> plant_class.Plant:
    new_plant = plant_class.Plant("images/plants/peashooter.png", {"x": 67, "y":67}, 67)
    new_plant.is_null = True
    return new_plant


def get_spawn_pos(looking_for_pos: dict[str,int], start_pos: dict[str,int], offsets: dict[str,int], total_positions: dict[str,int]) -> dict[str,int]:
    return_x_pos:int = start_pos["x"] + (offsets["x"] * looking_for_pos["x"])
    return_y_pos:int = start_pos["y"] + (offsets["y"] * looking_for_pos["y"])
    return {"x": return_x_pos, "y": return_y_pos}

def is_square_occupied(board: Board, position: dict[str, int]):
    legal_moves = board.legal_moves
    return not legal_moves[position["x"]][position["y"]]

def is_in_range(position: dict[str,int]) -> bool:
    if position["x"] > 8 or position["x"] < 0 or position["y"] > 4 or position["y"] < 0:
        return False
    else:
        return True

class Board(object):
    legal_moves: list[list[bool]] = []
    plants: list[list[object]] = []
    def __init__(self: Board, rows:int, columns:int) -> None:
        for i in range(rows + 1):
            LM_to_append_list: list[bool] = []
            PLA_to_append_list: list = []
            for j in range(columns + 1 ):
                LM_to_append_list.append(True)
                PLA_to_append_list.append(None)
            
            self.legal_moves.append(LM_to_append_list)
            self.plants.append(PLA_to_append_list)

