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

select * from autores;
/*inserindo info na coluna*/
insert into autores 
(nome,idade) values (' William P. Young','69');

/*atualizar informacoes*/
update autores
set idade = 50
where id = 3;

/*add coluna livros*/
alter table livros
add column id_autor int not null
after nome;

select * from livros;
insert into livros 
(nome,id_autor,preco, id_categoria) values ('Crepúsculo',3,20.99,3),('Diário de um Banana',2,20.99,4),('Turma da Mônica Jovem',1,20.99,5),('A Cabana',4,20.99,1);

/*juntar as 3 tabelas*/
select l.id, l.nome, l.preco, c.nome as categoria, a.nome as autor from livros as l
inner join categorias as c on c.id = l.id_categoria
inner join autores as a on a.id = l.id_autor
