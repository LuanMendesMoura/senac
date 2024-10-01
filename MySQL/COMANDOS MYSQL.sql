/*CRIACAO DE DATA BASE*/
create database delivery;
use delivery;

/*----------------------------------------------------------------------*/

/*CRIACAO DE TABELAS*/
create table produtos (
	id int primary key auto_increment unique not null,
    nome varchar(50) not null,
    id_categoria int not null,
    preco float not null,
    id_loja int not null
);

create table categorias (
	id int primary key auto_increment unique not null,
    nome varchar(50) not null
);

create table lojas (
	id int primary key auto_increment unique not null,
    nome varchar(50) not null,
    descricao longtext null,
    cpf varchar(50) not null
);

/*----------------------------------------------------------------------*/

/*INSERINDO INFORMACOES NAS TABELAS*/
insert into produtos (nome,id_categoria,preco,id_loja)
values ('Copo de Açai',2,7.99,2);
values ('Hamburguer Amigão',1,19.99,1);

insert into categorias (nome)
values ('Doce')
values ('Fast Food');

insert into lojas (nome,descricao,cpf)
values ('Açaiteria','Melhor açai de São Paulo','299.999.999-99');
values ('Amigao','Delivery de fast food para todos de SP','199.999.999-99');

/*----------------------------------------------------------------------*/

/*MOSTRANDO TODAS AS COLUNAS DAS TABELAS */
select * from produtos;

select * from categorias;

select * from lojas;

/*----------------------------------------------------------------------*/

/*INNER JOIN DE TODAS AS TABELAS E SUAS COLUNAS*/
select * from produtos
inner join categorias
inner join lojas;

/*----------------------------------------------------------------------*/

/*INNER JOIN * (GERAL)*/
select p.id, p.nome, c.nome, p.preco, l.nome from produtos as p
inner join categorias as c on c.id = p.id_categoria
inner join lojas as l on l.id = p.id_loja;

/*----------------------------------------------------------------------*/

/*INNER JOIN COM WHERE*/
select p.id, p.nome, c.nome, p.preco, l.nome from produtos as p
inner join categorias as c on c.id = p.id_categoria
inner join lojas as l on l.id = p.id_loja
where c.nome = 'Fast Food';

/*-----------------------------------------------------------------------*/

/*ADICIONAR COLUNAS NA TABELA*/
alter table produtos
add column descricao float not null
after id_categoria;

/*-----------------------------------------------------------------------*/

/*DELETAR COLUNA DA TABELA*/
alter table produtos 
drop column descricao;

/*-----------------------------------------------------------------------*/

/*RENOMEAR TABELA*/
rename table mercadorias to produtos;

/*-----------------------------------------------------------------------*/

/*ATUALIZAR INFORMACOES*/
update lojas
set nome = 'Joojue Açaiteria'
where id = 2; 

/*-----------------------------------------------------------------------*/

/*RENOMEAR COLUNA*/
alter table produtos 
change column nome nome_produto varchar(50) not null;

/*-----------------------------------------------------------------------*/