import psycopg2 as psycopg
from classes.game_stats import GameStats



def main_proxy():
    get_stats_from_db(1,1)
    # insert_stats(gen_test_game_stats())


def insert_stats(game_stats: GameStats) -> dict[str,int]:
    
    with get_connection() as connection:
        
        cursor = connection.cursor()
        
        #create player if neccecary
        name_test_query = f"""
        SELECT id
        FROM player
        WHERE name = '{game_stats.name}';
        """
        
        cursor.execute(name_test_query)
        name_test_results: list = cursor.fetchall()
        

        if len(name_test_results) == 0:
            #player doesnt exist, make player
            name_gen_query = f"""
            INSERT INTO player (name)
            VALUES ('{game_stats.name}')
            RETURNING id;
            """

            cursor.execute(name_gen_query)
            name_test_results = cursor.fetchall()

        player_id = name_test_results[0][0] #for some reason it started returning tuples??????????????? grab the first index of the tuple



        #create game
        game_gen_query = f"""
            INSERT INTO game (collected_sun, survived_time, plants_eaten, zombies_killed)
            VALUES ({game_stats.sun_collected}, {game_stats.time_survived}, {game_stats.plants_eaten}, {game_stats.zombies_killed})
            RETURNING id;"""

        cursor.execute(game_gen_query)
        game_id = cursor.fetchall()[0][0]


        

        #insert into player_game
        game_player_query = f"""
            INSERT INTO player_game (player_id, game_id)
            VALUES ({player_id}, {game_id});
            """
        
        cursor.execute(game_player_query)


        
        #insert into zombie_game
        #get id of type
        zombie_type_ids: list[int] = []
        for zombie_type in game_stats.killed_zombie_types.keys():
            zombie_type_id_query = f"""
            SELECT id
            FROM zombie_type
            WHERE name = '{zombie_type}';
            """
            cursor.execute(zombie_type_id_query)
            zombie_type_id = cursor.fetchall()[0][0]

            for i in range(game_stats.killed_zombie_types[zombie_type]):
                zombie_query = f"""
                INSERT INTO zombie (type, game)
                VALUES ({zombie_type_id}, {game_id});
                """

                cursor.execute(zombie_query)
            

        for plant_type in game_stats.plant_planted_types.keys():
                plant_type_id_query = f"""
                SELECT id
                FROM plant_type
                WHERE name = '{plant_type}';
                """
                cursor.execute(plant_type_id_query)
                plant_type_id = cursor.fetchall()[0][0]

                for i in range(game_stats.plant_planted_types[plant_type]):
                    plant_query = f"""
                    INSERT INTO plant (type, game)
                    VALUES ({plant_type_id}, {game_id});
                    """

                    cursor.execute(plant_query)
    
    return {"player id": player_id, "game id": game_id}

def get_stats_from_db_from_name(player_name: str, game_id: int) -> dict:
    with get_connection() as connection:
        cursor = connection.cursor()
        name_id_query = f"""
        SELECT id
        FROM player
        WHERE name = '({player_name})';
        """
        cursor.execute(name_id_query)
        name_id = cursor.fetchall()[0][0]
        return get_stats_from_db(name_id, game_id)

def get_stats_from_db(player_id: int, game_id:int) -> dict:
    with get_connection() as connection:
        cursor = connection.cursor()
        return_dict: dict = {}
        game_get_query = f"""
        SELECT collected_sun, survived_time, plants_eaten, zombies_killed
        FROM game
        WHERE id = {game_id};
        """

        cursor.execute(game_get_query)
        cursor_results = cursor.fetchall()

        return_dict["collected sun"] = cursor_results[0][0]
        return_dict["survived time"] = cursor_results[0][1]
        return_dict["plants eaten"] = cursor_results[0][2]
        return_dict["zombies_killed"] = cursor_results[0][3]



        zombie_query: str = f"""
        SELECT zombie_type.name FROM zombie INNER JOIN
        zombie_type ON zombie.type = zombie_type.id
        WHERE zombie.game = {game_id};"""
        zombie_types_query: str = f"""
        SELECT name FROM zombie_type;"""

        return_dict["favorite zombie"] = get_favorite_type(cursor, zombie_types_query, zombie_query, "no zombies killed!")



        plant_query: str = f"""
        SELECT plant_type.name FROM plant INNER JOIN
        plant_type ON plant.type = plant_type.id
        WHERE plant.game = {game_id};"""
        plant_types_query: str = f"""
        SELECT name FROM plant_type;"""

        return_dict["favorite plant"] = get_favorite_type(cursor, plant_types_query, plant_query, "no plants planted!")


        print(return_dict)
        return return_dict

def get_favorite_type(cursor, type_query: str, member_query: str, error_message: str) -> str:
    favorite_type: dict = {"type": "NO FAVORITE FOUND", "amount": -1}
    
    member_list: list = []
    cursor.execute(member_query)
    member_list = tuple_list_to_list(cursor.fetchall()) 

    type_list: list = []
    cursor.execute(type_query)
    type_list = tuple_list_to_list(cursor.fetchall()) 
    
    for type in type_list:
        count_of_this_type = member_list.count(type)
        if favorite_type["amount"] < count_of_this_type:
            favorite_type["type"] = type
            favorite_type["amount"] = count_of_this_type
    
    if favorite_type["type"] == "NO FAVORITE FOUND":
            favorite_type["type"] = "no plants planted!"
    return favorite_type["type"]

def tuple_list_to_list(tuple_list) -> list:
    return_list: list = []
    for tuple in tuple_list:
            return_list.append(tuple[0])
    return return_list


def get_connection():
    return psycopg.connect(
        dbname="pvz",
        user="postgres",
        password="postgres",
        host="localhost" )

def gen_test_game_stats() -> GameStats:
    new_game_stats = GameStats()
    
    new_game_stats.name = "READ_TEST_V1"

    new_game_stats.plants_eaten = 67 
    new_game_stats.plants_planted = 67
    new_game_stats.plant_planted_types = {"peashooter": 20, "repeater": 10}

    new_game_stats.zombies_killed = 30
    new_game_stats.killed_zombie_types = {"basic": 10, "conehead": 20}

    new_game_stats.time_survived = 8000000000

    new_game_stats.sun_collected = 2


    return new_game_stats