CREATE TABLE games (
game_id SERIAL PRIMARY KEY,
player1 VARCHAR(255),
player2 VARCHAR(255),
player3 VARCHAR(255),
player4 VARCHAR(255),
player5 VARCHAR(255),
game_date date,
winner VARCHAR(255)
);

CREATE TABLE specific_games (
game_id SERIAL PRIMARY KEY,
player VARCHAR(255),
terra_points INTEGER NOT NULL,
milestones INTEGER NULL,
first_place_awards INTEGER NULL,
second_place_awards INTEGER NULL,
forests INTEGER NULL,
city_points INTEGER NULL,
project_points INTEGER NULL,
total INTEGER NULL
);