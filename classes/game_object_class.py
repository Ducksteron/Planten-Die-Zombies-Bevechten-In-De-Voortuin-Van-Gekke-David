import pygame

class GameObject():
    collision_layer:int = -1
    collision_rect: pygame.Rect = pygame.Rect(0,0,0,0)
    is_null:bool = False
    def process(self: GameObject, delta_time: float) -> None:
        pass

    def on_collision(self: GameObject, collision_body: GameObject) -> None:
        pass
