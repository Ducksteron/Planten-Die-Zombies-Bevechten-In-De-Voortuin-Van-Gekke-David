import pygame
from managers import text_renderer

def show_final_stats(screen: pygame.Surface, loaded_font: pygame.Font, data_dict: dict) -> None:
    text_start = {"x": 100, "y": 200}
    text_offset = 50

    displayed_text_array: list[str] = [
        ("collected sun = " +  str(data_dict["collected sun"])),
        ("survived time = " + str(data_dict["survived time"])),
        ("plants eaten = " + str(data_dict["plants eaten"])),
        ("zombies killed = " + str(data_dict["zombies_killed"])),
        ("most killed zombie = " + str(data_dict["favorite zombie"])),
        ("favorite plant = " + str(data_dict["favorite plant"]))

    ]

    for to_display_text_index in range(len(displayed_text_array)):
        to_display_text = displayed_text_array[to_display_text_index]
        stack_text(to_display_text, text_start, text_offset, to_display_text_index, screen, loaded_font)



def stack_text(displayed_text: str, start: dict[str,int], offset: int, place: int, screen: pygame.Surface, loaded_font: pygame.Font):
    text_pos: dict[str,int] = {"x": start["x"]}
    text_pos["y"] = start["y"] + offset * (place + 1)
    text_renderer.render_text(screen,displayed_text, loaded_font, text_pos, pygame.Color(255,255,255,255))