CREATE TABLE player(
	id SERIAL PRIMARY KEY,
	name VARCHAR UNIQUE NOT NULL
);

CREATE TABLE game(
	id SERIAL PRIMARY KEY,
	player INT,
	collected_sun FLOAT,
	survived_time FLOAT,
	plants_eaten INT,
	zombies_killed INT,
	CONSTRAINT fk_player FOREIGN KEY (player) REFERENCES player(id)
);

CREATE TABLE plant_type (
	id SERIAL PRIMARY KEY,
	name VARCHAR UNIQUE NOT NULL
);

CREATE TABLE zombie_type (
	id SERIAL PRIMARY KEY,
	name VARCHAR UNIQUE NOT NULL
);

CREATE TABLE zombie (
	id SERIAL PRIMARY KEY,
	type INTEGER,
	game INTEGER,
	CONSTRAINT fk_zombie_type FOREIGN KEY (type) REFERENCES zombie_type(id),
	CONSTRAINT fk_game FOREIGN KEY (game) REFERENCES game(id)
);

CREATE TABLE plant (
	id SERIAL PRIMARY KEY,
	type INTEGER,
	game INTEGER,
	CONSTRAINT fk_plant_type FOREIGN KEY (type) REFERENCES plant_type(id),
	CONSTRAINT fk_game FOREIGN KEY (game) REFERENCES game(id)
);



--tabellen vullen
INSERT INTO plant_type (id,name) 
VALUES  (1, 'peashooter'),
		(2, 'repeater');


INSERT INTO zombie_type (id,name) 
VALUES  (1, 'basic'),
		(2, 'conehead');