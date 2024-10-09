/*DDL para criar banco de dados*/
drop database biblioteca;
create database biblioteca;
use biblioteca;

/*criacao de tabelas*/
create table categorias(
	id int primary key auto_increment not null,
    nome varchar(50) not null
);

create table autores(
	id int primary key auto_increment not null,
    nome varchar(50) not null,
    idade int not null
);

create table livros(
	id int primary key auto_increment not null,
    nome varchar(50) not null,
    id_autor int not null,
    preco float not null,
    id_categoria int not null
);

/*selecionando e inserindo informacoes na coluna*/
select * from categorias;
insert into categorias (nome) 
values ('Suspense'),('Drama'),('Romance'),('Diário'),('HQ');

select * from autores;
insert into autores (nome,idade) 
values ('Mauricio de Sousa',88),('Jeff Kinney',53),('Stephenie Meyer',50),(' William P. Young',69);

select * from livros;
insert into livros (nome,id_autor,preco, id_categoria) 
values ('Crepúsculo',3,20.99,3),('Diário de um Banana',2,20.99,4),('Turma da Mônica Jovem',1,20.99,5),('A Cabana',4,20.99,1);

/*juntar as 3 tabelas*/
select l.id, l.nome, l.preco, c.nome as categoria, a.nome as autor from livros as l
inner join categorias as c on c.id = l.id_categoria
inner join autores as a on a.id = l.id_autor;

select distinct preco from livros