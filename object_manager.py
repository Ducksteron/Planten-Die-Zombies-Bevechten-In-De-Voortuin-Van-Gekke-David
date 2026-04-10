import plant_class
    

def process_objects(all_objects: list[plant_class.GameObject],delta_time: float) -> None:
    for object in all_objects:
        object.process(delta_time)

def draw_objects(all_objects: list[plant_class.GameObject], screen) -> None:
    for object in all_objects:
        if issubclass(type(object), plant_class.RenderableObject):
            object.draw(screen) # type: ignore