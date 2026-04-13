import pygame
from managers import plant_plant as planter
from managers import render_image_wrapper as renderer

def handle_input(screen) -> dict: #screen is passed for debugging
    plant_mouse_button: int = 1
    remove_mouse_button: int = 3

    return_dict: dict = {"position": {}, "event": "EMPTY", "event_happened": False}

    rects = get_mouse_rects({"x":70, "y":70},{"x":9, "y":5}, {"x":80,"y":100})
    for rectangle_pos_string in rects.keys():
        rect_pos = str_to_pos_dict(rectangle_pos_string)
        rect = rects[rectangle_pos_string]
        # pygame.draw.rect(screen, (255,0,0), rect, 4)
        if rect.collidepoint(pygame.mouse.get_pos()):
            # pygame.draw.rect(screen, (255,255,0), rect, 4)

            events = pygame.event.get()
            for event in events:
                if not event.type == pygame.MOUSEBUTTONDOWN:
                    return return_dict
                
                if event.button == plant_mouse_button:
                    return_dict["position"] = rect_pos
                    return_dict["event"] = "plant"
                    return_dict["event_happened"] = True
                elif event.button == remove_mouse_button:
                    return_dict["position"] = rect_pos
                    return_dict["event"] = "remove"
                    return_dict["event_happened"] = True
    
    return return_dict
    

def get_mouse_rects( start_pos: dict[str,int], total_positions: dict[str,int], size:dict[str, int]) -> dict[str, pygame.Rect]:
    return_dict: dict[str, pygame.Rect] = {}
    for column in range(total_positions["y"]):
        for row in range(total_positions["x"]):
            # return_x_pos:int = start_pos["x"] + offsets["x"]
            # return_y_pos:int = start_pos["y"] + offsets["y"]
            pos: dict[str, int] = {"x": start_pos["x"] + (size["x"] * row), "y": start_pos["y"] + (size["y"] * column)}
            new_rect = pygame.Rect(pos["x"], pos["y"], size["x"],size["y"])
            return_dict[(str(row) + "|" + str(column)) ] = new_rect

    return return_dict

def str_to_pos_dict(string:str) -> dict[str,int]:
    segments = string.split("|")
    return {"x": int(segments[0]), "y": int(segments[1])}