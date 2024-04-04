-------------------------------------------------------------------------------------------
/*
Feito por ZAC MILIOLI
Data 03/04/2024
Aula 05 Modelagem de Bancos de Dados Relacionais
SSMS
*/
-------------------------------------------------------------------------------------------

CREATE DATABASE correios;

USE correios;

SELECT * FROM cep;

ALTER TABLE cep ADD id INT IDENTITY;

-------------------------------------------------------------------------------------------

CREATE TABLE cidade(
id int primary key identity,
city varchar(100) not null,
estado nvarchar(2) not null
)

INSERT INTO cidade(city, estado) SELECT DISTINCT cep.city, cep.estado FROM cep 

UPDATE cep SET cep.city=cidade.id FROM cidade INNER JOIN cep ON cep.city=cidade.city

select * from cidade

-------------------------------------------------------------------------------------------

CREATE TABLE logradouro(
id int primary key identity,
descricao varchar(100) not null,
cep int not null,
id_cidade int not null,
constraint fk_cidade foreign key (id_cidade) references cidade(id)
) 

INSERT INTO logradouro(descricao, cep, id_cidade) 
SELECT DISTINCT cep.vicinity, cep.cep, cidade.id FROM cep 
INNER JOIN cidade ON cidade.id=cep.city

SELECT * FROM logradouro ORDER BY id

-------------------------------------------------------------------------------------------

DROP TABLE cep CEP.txt 