from classes import game_object_class
from classes import renderable_object_class
    

def process_objects(all_objects: list[game_object_class.GameObject],delta_time: float) -> None:
    for object in all_objects:
        object.process(delta_time)

def draw_objects(all_objects: list[game_object_class.GameObject], screen) -> None:
    for object in all_objects:
        if issubclass(type(object), renderable_object_class.RenderableObject):
            object.draw(screen) # type: ignore