import psycopg2 as psycopg
from classes.game_stats import GameStats


def insert_stats(game_stats: GameStats) -> dict[str,int]:
    
    with get_connection() as connection:
        with connection.cursor() as cursor:
            
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
                INSERT INTO game (player, collected_sun, survived_time, plants_eaten, zombies_killed)
                VALUES ({player_id},{game_stats.sun_collected}, {game_stats.time_survived}, {game_stats.plants_eaten}, {game_stats.zombies_killed})
                RETURNING id;"""

            cursor.execute(game_gen_query)
            game_id = cursor.fetchall()[0][0]


            
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

def get_stats_from_db(player_id: int, game_id:int) -> dict:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            return_dict: dict = {}
            game_get_query = f"""
            SELECT 
                CAST(game.collected_sun AS BIGINT) AS "collected sun", 
                CAST(game.survived_time AS BIGINT) AS "survived time", 
                game.plants_eaten, game.zombies_killed,
                (SELECT 
                    zombie_type.name AS "most killed zombie"
                FROM 
                    zombie
                    INNER JOIN zombie_type ON zombie.type = zombie_type.id
                WHERE
                    zombie.game = game.id
                GROUP BY
                    zombie_type.name
                ORDER BY
                    COUNT(zombie_type.name) DESC
                LIMIT 1),

                (SELECT 
                    plant_type.name AS "favorite plant"
                FROM 
                    plant
                    INNER JOIN plant_type ON plant.type = plant_type.id
                WHERE
                    plant.game = game.id
                GROUP BY
                    plant_type.name
                ORDER BY
                    COUNT(plant_type.name) DESC
                LIMIT 1),

                CAST((SELECT DISTINCT ON (player.name) 
                    game.survived_time AS "high score"
                FROM
                    game 
                    INNER JOIN player ON player.id = game.player
                WHERE 
                    player.id = {player_id}
                ORDER BY 
                    "name", "high score" DESC) AS BIGINT)
                
            FROM 
                game
            WHERE
                game.id = {game_id};
            """

            cursor.execute(game_get_query)
            cursor_results = cursor.fetchall()

            return_dict["collected sun"] = cursor_results[0][0]
            return_dict["survived time"] = cursor_results[0][1]
            return_dict["plants eaten"] = cursor_results[0][2]
            return_dict["zombies_killed"] = cursor_results[0][3]
            return_dict["favorite zombie"] = cursor_results[0][4]
            return_dict["favorite plant"] = cursor_results[0][5]
            return_dict["high score"] = cursor_results[0][6]

            return return_dict

def get_leaderboard(list_length:int = 3) -> list[dict[str,int]]:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            return_leaderboard:list[dict[str,int]] = []
            leaderboard_get_query = f"""
            SELECT 
                *
            FROM 
                (SELECT DISTINCT ON (player.name) 
                    player.name AS "name", 
                    CAST(game.survived_time AS BIGINT) AS "high score" 
                FROM
                    game 
                    INNER JOIN player ON player.id = game.player
                ORDER BY 
                "name", "high score" DESC)
            ORDER BY
                "high score" DESC
            LIMIT {list_length};
            """

            cursor.execute(leaderboard_get_query)
            cursor_results = cursor.fetchall()
            
            for data_tuple_index in range(len(cursor_results)):
                return_leaderboard.append({cursor_results[data_tuple_index][0]: cursor_results[data_tuple_index][1]})


    return return_leaderboard

def get_connection():
    return psycopg.connect(
        dbname="pvz",
        user="postgres",
        password="postgres",
        host="localhost" )

def gen_test_game_stats() -> GameStats:
    new_game_stats = GameStats()
    
    new_game_stats.name = "xX_N00BSL4YER_Xx"

    new_game_stats.plants_eaten = 78
    new_game_stats.plants_planted = 57
    new_game_stats.plant_planted_types = {"peashooter": 20, "repeater": 10}

    new_game_stats.zombies_killed = 1
    new_game_stats.killed_zombie_types = {"basic": 10, "conehead": 20}

    new_game_stats.time_survived = 3489

    new_game_stats.sun_collected = 2


    return new_game_stats

def insert_buncha_stuff() -> None:
     for i in range(1):
          insert_stats(gen_test_game_stats())