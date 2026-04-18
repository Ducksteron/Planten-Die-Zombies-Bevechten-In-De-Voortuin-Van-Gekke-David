
class GameStats():
    name: str = ""

    plants_eaten: int = 0 
    plants_planted: int = 0
    plant_planted_types: dict[str,int] = {}

    zombies_killed: int = 0
    killed_zombie_types: dict[str,int] = {}

    time_survived: float = 0.0

    sun_collected: float = 0.0

    def add_plant_type(self: GameStats, type: str):
        if not type in self.plant_planted_types:
            self.plant_planted_types[type] = 1
        else:
            self.plant_planted_types[type] += 1
    
    def add_zombie_type(self: GameStats, type: str):
        if not type in self.killed_zombie_types:
            self.killed_zombie_types[type] = 1
        else:
            self.killed_zombie_types[type] += 1
    
    def set_name(self: GameStats, new_name: str):
        self.name = new_name.replace("'", "''")

