/*
Criado por ZAC MILIOLI
Data: 20/03/2024
Feito para a aula de Banco de Dados
SSMS
*/



CREATE DATABASE AulaNova;
USE AulaNova;




-- Manipulção Livro
CREATE TABLE Livro (
Indentificador INT PRIMARY KEY IDENTITY(1,1),
Titulo VARCHAR(100) NOT NULL,
N_paginas INT NOT NULL,
Lancamento DATE NOT NULL
);

SELECT * FROM Livro;

TRUNCATE TABLE Livro;

ALTER TABLE Livro ADD id_autor INT;
ALTER TABLE Livro ADD FOREIGN KEY (id_autor) REFERENCES Autor (Identificador);

INSERT INTO Livro (Titulo, N_paginas, Lancamento, id_autor) 
VALUES ('A Masmorra de Zacarias', 163, '1995/05/06', 1);

INSERT INTO Livro (Titulo, N_paginas, Lancamento, id_autor) 
VALUES ('As Brumas de Chatisse', 890, '1850/01/01', 2);

INSERT INTO Livro (Titulo, N_paginas, Lancamento, id_autor) 
VALUES ('Como Ser um Coach e Roubar Grana de Otario', 52, '2015/12/25', 3);

INSERT INTO Livro (Titulo, N_paginas, Lancamento, id_autor) 
VALUES ('Biblia', 1200, '0020/01/01', NULL);

SELECT Livro.Titulo, Livro.N_paginas, Livro.Lancamento, Autor.Nome FROM Livro INNER JOIN Autor ON Livro.id_autor = Autor.Identificador;

SELECT Livro.Titulo, Livro.N_paginas, Livro.Lancamento, Autor.Nome FROM Livro LEFT JOIN Autor ON Livro.id_autor = Autor.Identificador;

SELECT Livro.Titulo, Livro.N_paginas, Livro.Lancamento, Autor.Nome FROM Livro LEFT JOIN Autor ON Livro.id_autor = Autor.Identificador WHERE Autor.Nome IS NULL;

SELECT Autor.Nome, Livro.Titulo, Livro.Lancamento FROM Autor LEFT JOIN Livro ON Autor.Identificador = Livro.id_autor;


-- Manipulação Autor
CREATE TABLE Autor (
Identificador INT PRIMARY KEY IDENTITY(1,1),
Nome VARCHAR(100) NOT NULL
);

SELECT * FROM Autor;

TRUNCATE TABLE Autor;

INSERT INTO Autor (Nome) 
VALUES ('Pedro Vai de Caminha');

INSERT INTO Autor (Nome) 
VALUES ('Deide Costa');

INSERT INTO Autor (Nome) 
VALUES ('Filosofo Piton');

INSERT INTO Autor (Nome) 
VALUES ('Mancebo e o Copo');