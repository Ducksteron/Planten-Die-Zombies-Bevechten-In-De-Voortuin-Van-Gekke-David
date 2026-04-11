from classes import renderable_object_class as ROC

class Zombie(ROC.RenderableObject):
    def __init__(self: Zombie,image_path: str, pos:dict[str,int]):
        super().__init__(image_path, pos)

   
    def process(self: Zombie, delta_time: float) -> None:
        super().process(delta_time)
    
        self.pos = {"x": self.pos["x"] - 100 * delta_time, "y": self.pos["y"]}
        if self.pos["x"] < -100:
            self.is_null = True
