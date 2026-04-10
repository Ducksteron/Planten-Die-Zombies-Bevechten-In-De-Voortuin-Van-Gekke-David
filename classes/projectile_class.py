from classes import renderable_object_class

class Projectile(renderable_object_class.RenderableObject):
    def __init__(self: Projectile, image_path: str, pos:dict[str,int]) -> None:
        super().__init__(image_path, pos)

    def draw(self: Projectile,screen, use_given_trans_dict:bool = False, given_trans_dict: dict[str,dict] = {}) -> None:
        super().draw(screen, use_given_trans_dict, given_trans_dict)
    
    def move(self: Projectile, delta_time: float) -> None:
        self.pos = {"x": self.pos["x"] + 10 * delta_time, "y": self.pos["y"]}
    
    def process(self: Projectile, delta_time: float) -> None:
        super().process(delta_time)
        self.move(delta_time)