import pygame
from managers import text_renderer

def show_final_stats(screen: pygame.Surface, loaded_font: pygame.Font, data_dict: dict, inputs: list, is_displaying_LB: bool, leaderboard: list[dict[str,int]], position_in_leaderboard:int) -> bool:
    text_start = {"x": 100, "y": 150}
    text_offset = 50
    
    for event in inputs:
        if not event.type == pygame.KEYDOWN: continue
        if event.unicode == " ":
            is_displaying_LB = not is_displaying_LB


    displayed_text_array: list[str] = []
    
    if is_displaying_LB:
        displayed_text_array = ["leaderboard"]
        for LB_entry in leaderboard:
            displayed_text_array.append(stringable_dict_to_str(LB_entry))
        displayed_text_array.append("")
        displayed_text_array.append(("Your position in leaderboard = " + str(position_in_leaderboard)))
    else:
        displayed_text_array  = [
            ("high score = " +  str(data_dict["high score"])),
            ("survived time (score) = " + str(data_dict["survived time"])),
            ("collected sun = " +  str(data_dict["collected sun"])),
            ("plants eaten = " + str(data_dict["plants eaten"])),
            ("zombies killed = " + str(data_dict["zombies_killed"])),
            ("most killed zombie = " + str(data_dict["favorite zombie"])),
            ("favorite plant = " + str(data_dict["favorite plant"]))
        ]

    for to_display_text_index in range(len(displayed_text_array)):
        to_display_text = displayed_text_array[to_display_text_index]
        stack_text(to_display_text, text_start, text_offset, to_display_text_index, screen, loaded_font)
    
    return is_displaying_LB


def stringable_dict_to_str(dict) -> str:
    return_string: str = ""
    for key in list(dict.keys()):
        return_string += str(key)
        return_string += " "
        return_string += str(dict[key])
    return return_string



def stack_text(displayed_text: str, start: dict[str,int], offset: int, place: int, screen: pygame.Surface, loaded_font: pygame.Font):
    text_pos: dict[str,int] = {"x": start["x"]}
    text_pos["y"] = start["y"] + offset * (place + 1)
    text_renderer.render_text(screen,displayed_text, loaded_font, text_pos, pygame.Color(255,255,255,255))