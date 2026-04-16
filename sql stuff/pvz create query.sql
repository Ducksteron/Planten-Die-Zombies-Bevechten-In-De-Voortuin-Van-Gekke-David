CREATE TABLE player(
	id SERIAL PRIMARY KEY,
	name VARCHAR
);

CREATE TABLE game(
	id SERIAL PRIMARY KEY,
	collected_sun FLOAT
);

CREATE TABLE plant_type (
	id SERIAL PRIMARY KEY,
	name VARCHAR
);

CREATE TABLE zombie_type (
	id SERIAL PRIMARY KEY,
	name VARCHAR
);

CREATE TABLE zombie (
	id SERIAL PRIMARY KEY,
	type INTEGER,
	CONSTRAINT fk_zombie_type FOREIGN KEY (type) REFERENCES zombie_type(id)
);

CREATE TABLE plant (
	id SERIAL PRIMARY KEY,
	type INTEGER,
	CONSTRAINT fk_plant_type FOREIGN KEY (type) REFERENCES plant_type(id)
);


CREATE TABLE player_game (
	player_id INT,
	game_id INT,
	CONSTRAINT fk_player_id FOREIGN KEY (player_id) REFERENCES player(id),
	CONSTRAINT fk_game_id FOREIGN KEY (game_id) REFERENCES game(id)
);

CREATE TABLE zombie_game (
	zombie_id INT,
	game_id INT,
	CONSTRAINT fk_zombie_id FOREIGN KEY (zombie_id) REFERENCES zombie(id),
	CONSTRAINT fk_game_id FOREIGN KEY (game_id) REFERENCES game(id)
);

CREATE TABLE plant_game (
	plant_id INT,
	game_id INT,
	CONSTRAINT fk_plant_id FOREIGN KEY (plant_id) REFERENCES plant(id),
	CONSTRAINT fk_game_id FOREIGN KEY (game_id) REFERENCES game(id)
);


