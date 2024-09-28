/*DDL para criar banco de dados*/
create database biblioteca;
use biblioteca;

/*criacao de colunas*/
create table categorias(
	id int primary key auto_increment not null,
    nome varchar(50) not null
);

create table clientes(
	id int primary key auto_increment not null,
    cpf varchar(20) not null,
    telefone int8 not null,
    nome varchar(50) not null,
    id_livro int not null
);

create table livros(
	id int primary key auto_increment not null,
    nome varchar(50) not null,
    id_categoria int not null
);

/*add nova coluna*/
alter table livros
add column preco float not null
after nome;

/*renomear tabela*/
rename table clientes to autores;

/*deletar coluna da tabela*/
ALTER TABLE `biblioteca`.`autores` 
DROP COLUMN `id_livro`;

select * from categorias;
insert into categorias (nome) values ('HQ');

select * from autores
insert into autores 
(nome,idade) values ('Mauricio de Sousa','88'),('Jeff Kinney','53'),('Crepusculo','Stephenie Meyer')

alter table autores
