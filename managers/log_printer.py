import pygame
from managers import logger

def handle_log_printing(input_events: list) -> None:
    for event in input_events:
        if not event.type == pygame.KEYDOWN:
            continue
        if event.unicode == "l":
            print(logger.read())
