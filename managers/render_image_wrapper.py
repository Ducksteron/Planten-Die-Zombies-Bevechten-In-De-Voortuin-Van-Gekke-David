import pygame

def render_from_path(screen, path: str, position: dict[str,int], transform_dict: dict = {}) -> pygame.Surface:
    image = pygame.image.load(path)
    return render(screen, image, position, transform_dict)

def render(screen, image: pygame.Surface, position: dict[str,int], transform_dict: dict = {}) -> pygame.Surface:
    position_x:int = position["x"]
    position_y:int = position["y"]
    
    
    image = transfrom_by_trans_dict(image, transform_dict)

    blit_pos = (0,0)

    if position_x == 0 and position_y == 0:
        blit_pos = image.get_rect()
    else:
        blit_pos = (position_x, position_y)

    screen.blit(image, blit_pos)

    return image

def transfrom_by_trans_dict(image: pygame.Surface, transform_dict: dict) -> pygame.Surface:
    if "flip" in transform_dict:
        flip_dict: dict = transform_dict["flip"]
        image = pygame.transform.flip(image, flip_dict["flip_x"], flip_dict["flip_y"])

    if "rotation" in transform_dict:
        rotation_dict: dict = transform_dict["rotation"]
        image = pygame.transform.rotate(image,rotation_dict["angle"])

    if "scale" in transform_dict:
        scale_dict: dict = transform_dict["scale"]
        image = pygame.transform.scale(image, (scale_dict["width"], scale_dict["height"]))

    if "scale by" in transform_dict:
        scale_by_dict: dict = transform_dict["scale by"]
        image = pygame.transform.scale_by(image, scale_by_dict["amount"])
    
    return image

def transform_rect_by_trans_dict(rect: pygame.Rect, transform_dict: dict):
    if "scale by" in transform_dict:
        scale_by_dict: dict = transform_dict["scale by"]
        rect = pygame.Rect.scale_by(rect, scale_by_dict["amount"])
    
    return rect





def scale_trans_dict(transform_dict: dict[str,dict], width: int = 1 , height:int = 1) -> dict:
    transform_dict["scale"] = {"width": width, "height": height}
    return transform_dict

def scale_by_trans_dict(transform_dict: dict[str,dict], amount:float) -> dict:
    transform_dict["scale by"] = {"amount": amount}
    return transform_dict

def flip_trans_dict(transform_dict: dict[str,dict], flip_x: bool = False , flip_y: bool = False) -> dict:
    transform_dict["flip"] = {"flip_x" : False , "flip_y" : False}
    return transform_dict

def rotate_trans_dict(transform_dict: dict[str,dict], angle:float = 0.0) -> dict:
    if "rotation" in transform_dict:
        transform_dict["rotation"] = {"angle": transform_dict["rotation"]["angle"] + angle}
    else:
        transform_dict["rotation"] = {"angle": angle}
    return transform_dict


