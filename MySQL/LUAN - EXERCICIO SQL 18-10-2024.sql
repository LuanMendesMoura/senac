drop database loja;
create database loja;
use loja;

create table produtos (
	id int primary key auto_increment,
    nome varchar(100),
    preco decimal(10,2),
    estoque int
);

create table clientes (
	id int primary key auto_increment,
    nome varchar(100),
    email varchar(100),
    cidade varchar(100)
);

create table vendas (
	id int primary key auto_increment,
    data_venda date,
    id_cliente int,
    id_produto int,
    quantidade int,
    valor_total decimal(10,2),
    foreign key (id_cliente) references clientes(id),
    foreign key (id_produto) references produtos(id)
);

/*-------------------------------------------------*/

insert into produtos (nome,preco,estoque)
values('Coca-cola Pet 2,5L',10.99,20),('Detergente Líquido Ypê 500ml',2.25,20),
('Café Pilão',24.78,20),('Achocolatado em Pó Nescau',8.27,20),
('Filtro de Papel Melitta',3.69,20),('Chá Matte Leão',5.29,20),
('Biscoito Cookies Bauducco',4.08,20),('Chiclete Trident 32g',6.29,20),
('Detergente em Pó Omo',11.98,20),('Tênis Nike',400,3);

insert into clientes (nome,email,cidade)
values('Luan','luan@hotmail.com','Campo Grande'),('Elias','elias@hotmail.com','Campo Grande'),
('Marcelina','marcelina@hotmail.com','Rio de Janeiro'),('Chris','chris@hotmail.com','São Paulo'),
('Luna','luna@hotmail.com','Campo Grande'),('Isabelle','isabelle@hotmail.com','Rio de Janeiro'),
('Lais','lais@hotmail.com','Três Lagoas'),('Francisco','francisco@hotmail.com','São Paulo'),
('João Silva','joaosilva@hotmail.com','São Paulo'),('Maria Souza','mariasouza@hotmail.com','São Paulo');

insert into vendas (data_venda,id_cliente,id_produto,quantidade,valor_total)
values('2024-10-01',1,1,3,32.97),('2024-10-01',2,6,3,15.87),
('2024-10-02',3,6,3,15.87),('2024-10-02',4,2,3,7.5),('2024-10-03',5,8,1,6.29),
('2024-10-03',6,8,5,31.45),('2024-10-04',7,9,2,23.96),('2024-10-05',8,4,2,16.54),('2024-10-01',9,1,4,43.96);

/*-------------------------EXERCICIO 1-------------------------*/
select nome, estoque from produtos;

/*-------------------------EXERCICIO 2-------------------------*/
select nome, email from clientes
where cidade = 'São Paulo';

/*-------------------------EXERCICIO 3-------------------------*/
select v.data_venda, p.nome, v.valor_total from clientes as c 
inner join vendas as v
on v.id_cliente = c.id
inner join produtos as p       
on p.id = v.id_produto
where c.nome = 'João Silva';

/*-------------------------EXERCICIO 4-------------------------*/
update produtos set preco = 349.99 where id = 10;
select * from produtos;

/*-------------------------EXERCICIO 5-------------------------*/
insert into produtos (nome, preco, estoque)
values ('Bola de Futebol Adidas',89.90,50);

/*-------------------------EXERCICIO 6-------------------------*/
select sum(quantidade) as VENDAS, sum(valor_total) as TOTAL from vendas
where data_venda = '2024-10-01';

/*-------------------------EXERCICIO 7-------------------------*/
select c.nome, v.valor_total from vendas as v
inner join clientes as c
on c.id = v.id_cliente;

/*-------------------------EXERCICIO 8-------------------------*/
update produtos set estoque = 15 where id = 8;

/*-------------------------EXERCICIO 9-------------------------*/
select p.nome, v.quantidade from vendas as v
inner join produtos as p
on p.id = v.id_produto
order by quantidade desc
limit 1;

/*-------------------------EXERCICIO 10-------------------------*/
insert into vendas (data_venda,id_cliente,id_produto,quantidade,valor_total)
values (current_date(),3,5,2,(select preco * 2 from produtos where id = 5));

/*-------------------------EXERCICIO 11-------------------------*/
select p.* from produtos as p
left join vendas as v 
on v.id_produto = p.id
where v.id_produto is null;

/*-------------------------EXERCICIO 12-------------------------*/
select v.data_venda, c.nome as clientes, v.valor_total from vendas as v
inner join clientes as c
on c.id = v.id_cliente;

/*-------------------------EXERCICIO 13-------------------------*/
select sum(estoque) 'estoque total'
from produtos;

/*-------------------------EXERCICIO 14-------------------------*/
select c.nome, v.valor_total from vendas as v
inner join clientes as c
on c.id = v.id_cliente
order by v.valor_total desc
limit 1;

/*-------------------------EXERCICIO 15-------------------------*/
update clientes set cidade = 'Rio de Janeiro' where id = 10