create database RPG;
use rpg;
CREATE TABLE Jogador ( 
 idjogador INT AUTO_INCREMENT primary key,  
 nome VARCHAR(100) NOT NULL,  
 senha INT(10)  
) default charset = utf8;

CREATE TABLE Personagem (
 idPersonagem INT primary KEY,
 nome VARCHAR(100) NOT NULL,  
 Raca VARCHAR(20),  
 Classe VARCHAR(20),  
 Descricao varchar(100),  
 idade int(3),
 sexo varchar(20)
) default charset = utf8;

CREATE TABLE ficha ( 
 idPersonagem INT,
 vida INT(3),  
 ataque INT(3),  
 defesa INT(3),  
 inteligencia INT(3),  
 carisma INT(3),  
 forca INT(3),  
 velocidade INT(3),  
 furtividade INT(3),
 foreign key (idPersonagem) references personagem(idPersonagem) on update cascade on delete cascade
) default charset = utf8;

CREATE TABLE Bolsa ( 
 idPersonagem INT,  
 item1 VARCHAR(50) default 'Vazio',
 item2 VARCHAR(50) default 'Vazio',
 item3 VARCHAR(50) default 'Vazio',
 item4 VARCHAR(50) default 'Vazio',
 item5 VARCHAR(50) default 'Vazio',
 item6 VARCHAR(50) default 'Vazio',
 dinheiro double default '0.0' ,
 foreign key (idPersonagem) references personagem(idPersonagem) on update cascade on delete cascade
) default charset = utf8;
