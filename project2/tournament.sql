-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
CREATE DATABASE tournament;

\c tournament;

DROP TABLE IF EXISTS players, matches CASCADE;

CREATE TABLE players (
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL
);


CREATE TABLE matches (
	id SERIAL PRIMARY KEY,
	winner_id INTEGER REFERENCES players (id),
	loser_id INTEGER REFERENCES players (id)
);

CREATE VIEW standings AS
	SELECT p.id, p.name, b.wins, count(m.id) AS matches 
	FROM players AS p 
	LEFT JOIN matches AS m 
	ON (p.id=m.winner_id OR p.id=m.loser_id) 
	JOIN (SELECT p.id, count(m.winner_id) AS wins FROM players AS p
		 LEFT JOIN matches AS m 
		 ON p.id=m.winner_id 
		 GROUP BY p.id) AS b 
	ON p.id = b.id 
	GROUP BY p.id, b.wins 
	ORDER BY b.wins DESC;
