--MADE USING AS REFERENCE https://www.youtube.com/watch?v=HXV3zeQKqGY&list=WL&index=17&t=8845s
--DEVELOPED AND MANIPULATED IN POPSQL

CREATE TABLE pkmn (
    pkmn_id INT AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    type VARCHAR(10) DEFAULT('Normal'),
    PRIMARY KEY(pkmn_id)
);

CREATE TABLE pkmn_weakness(
    weakness_id INT AUTO_INCREMENT,
    weak_to VARCHAR(10),
    weakness_id_fk INT,
    PRIMARY KEY (weakness_id),
    FOREIGN KEY (weakness_id_fk) REFERENCES pkmn(pkmn_id) ON DELETE SET NULL
);

DESCRIBE pkmn;

DROP TABLE pkmn;
DROP TABLE pkmn_weakness;

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
SELECT * FROM pkmn_weakness;

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


