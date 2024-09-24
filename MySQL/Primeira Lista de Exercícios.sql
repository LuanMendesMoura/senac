create table categorias(
	id int auto_increment, nome varchar(45) not null, primary key(id)
);

/*DENTRO DA DATABASE*/
use produtos;

insert into categorias(nome) value('Produtos de Limpeza'),('Bebida'),('Comida'); 
select * from categorias;

insert into produtos(nome,preco,id_categoria) 
values('Maça',5.99,3),('Desengordurante',6.99,1),('Banana',5.99,3),('Coca Cola',7.99,2),('Água',3.99,2),('Água Sanitária',7.99,1);
select * from produtos;

delete from produtos where id = 6;

select * from produtos where produtos.preco < 6;

delete from produtos where preco = 5.99 and id_categoria = 3; /*ERRO*/

select produtos.id, produtos.nome, produtos.preco, categorias.nome as 'categoria' from produtos
inner join categorias on categorias.id = produtos.id_categoria;

select produtos.id, produtos.nome, produtos.preco, categorias.nome as 'categoria' from produtos
inner join categorias on categorias.id = produtos.id_categoria
where categorias.id = 2;

select produtos.id, produtos.nome, produtos.preco, categorias.nome as 'categoria' from produtos
inner join categorias on categorias.id = produtos.id_categoria
where produtos.preco > 6 and categorias.id = 1;

