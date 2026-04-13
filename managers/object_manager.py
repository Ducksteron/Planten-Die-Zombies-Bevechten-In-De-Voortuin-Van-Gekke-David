from classes import game_object_class
from classes import renderable_object_class
from classes import plant_class

import pygame

def remove_null_instances(all_objects: list[game_object_class.GameObject], board) -> list[game_object_class.GameObject]:
    for object in all_objects:
        if object.is_null:
            if issubclass(type(object), plant_class.Plant): #remove plant from board so squares with eaten plants can be replanted
                from managers.plant_plant import Board #done here bc circular import error
                static_board: Board = board
                
                plant_object: plant_class.Plant = object #type: ignore
                plant_pos:dict[str,int] = plant_object.position
                if "x" in plant_pos: #some null plants dont have position and dont have to be cleared
                    static_board.legal_moves[plant_pos["x"]][plant_pos["y"]] = True
                    static_board.plants[plant_pos["x"]][plant_pos["y"]] = None

            all_objects.remove(object)
    return all_objects

def process_objects(all_objects: list[game_object_class.GameObject],delta_time: float) -> None:
    for object in all_objects:
        object.process(delta_time)

def draw_objects(all_objects: list[game_object_class.GameObject], screen) -> None:
    for object in all_objects:
        if issubclass(type(object), renderable_object_class.RenderableObject):
            if object.is_null:
                continue

            object.draw(screen) # type: ignore

def handle_collision(all_objects: list[game_object_class.GameObject]):
    object_col_layer_dict: dict[int, list[game_object_class.GameObject]] = {}
    for object in all_objects: #sort objects by collision layer
        if object.collision_layer == -1: #discard those without col layer
            continue
        if object.collision_rect == pygame.Rect(0,0,0,0): #discard without col rect
            continue
        
        if not (object.collision_layer in object_col_layer_dict):
            object_col_layer_dict[object.collision_layer] = []
        
        col_layer_object_list = object_col_layer_dict[object.collision_layer]
        col_layer_object_list.append(object)
        object_col_layer_dict[object.collision_layer] = col_layer_object_list

    for col_layer in object_col_layer_dict.keys(): #gets all objects of certain col layer
        objects = object_col_layer_dict[col_layer]

        #compares all objects to eachother to see if theyre colliding
        for first_object_index in range(len(objects)):
            first_object = objects[first_object_index]

            for second_object_index in range(len(objects)):
                if first_object_index == second_object_index: #dont compare object to itself
                    continue
                
                second_object = objects[second_object_index]

                #colliding so call on collision for both objects
                if first_object.collision_rect.colliderect(second_object.collision_rect):
                    first_object.on_collision(second_object)
                    second_object.on_collision(first_object)





def handle_shooting(all_objects: list[game_object_class.GameObject], delta_time: float) -> list[game_object_class.GameObject]:
    for object in all_objects:
        if issubclass(type(object), plant_class.Plant):
            all_objects.append(object.handle_shooting(delta_time)) # type: ignore
    
    return all_objects

def handle_zombies_eating(all_objects: list[game_object_class.GameObject], delta_time: float) -> None:
    for object in all_objects:
        from classes import zombie_class
        if issubclass(type(object), zombie_class.Zombie):
            object.handle_eating(delta_time) #type: ignore