CREATE TABLE pkmn (
    pkmn_id INT AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    type VARCHAR(10) DEFAULT 'Normal',
    PRIMARY KEY (pkmn_id)
);

DESCRIBE pkmn;

DROP TABLE pkmn;

ALTER TABLE pkmn ADD defense DECIMAL(2, 1);

ALTER TABLE pkmn DROP COLUMN defense;

INSERT INTO pkmn(name, type) VALUES('Pikachu', 'Eletrico');
INSERT INTO pkmn(name, type) VALUES('Bulbassauro', 'Planta');
INSERT INTO pkmn(name, type) VALUES('Charmander', 'Fogo');
INSERT INTO pkmn(name, type) VALUES('Squirtle', 'Agua');
INSERT INTO pkmn(name, type) VALUES('Dratini', 'Dragao');
INSERT INTO pkmn(name) VALUES('Ratatta');

UPDATE pkmn
SET type = 'Fogo'
WHERE type = 'Fire';

UPDATE pkmn
SET pkmn_id = 1
WHERE pkmn_id = 0;

UPDATE pkmn
SET type = 'Defensive'
WHERE type = 'Planta' OR type = 'Agua';

UPDATE pkmn
SET name = 'Dragonite', type = 'Dragao'
WHERE pkmn_id = 3;

DELETE FROM pkmn
WHERE name = 'Ratatta';



SELECT * FROM pkmn;

SELECT *
FROM pkmn
ORDER BY pkmn.type ASC, name ASC
LIMIT 3;

SELECT *
FROM pkmn
WHERE pkmn.type <> 'Normal' AND pkmn.pkmn_id > 2;

SELECT *
FROM pkmn
WHERE pkmn.name IN ('Dratini', 'Dragonite', 'Charmander');
