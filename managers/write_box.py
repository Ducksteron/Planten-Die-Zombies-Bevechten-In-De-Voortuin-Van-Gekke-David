import pygame
from classes.game_stats import GameStats


def handle_writing(base_text: str, writen_text: str, input_events:list, game_stats: GameStats) -> str:
    if game_stats.name != "":
        return (base_text + game_stats.name)
    new_text = writen_text.replace(base_text, "")
    return (base_text + get_writen_text(new_text,input_events, game_stats))

def get_writen_text(new_text:str,input_events:list, game_stats: GameStats) -> str:
    return_string: str = new_text
    for event in input_events:
        if event.type == pygame.KEYDOWN:

            # Check for backspace
            if event.key == pygame.K_BACKSPACE:

                # get text input from 0 to -1 i.e. end.
                return_string = return_string[:-1]

            elif event.key == pygame.K_RETURN and return_string != "":
                game_stats.name = return_string

            # Unicode standard is used for string
            # formation
            else:
                return_string += event.unicode

    return return_string
