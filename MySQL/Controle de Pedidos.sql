drop database loja;
create database loja;
use loja;

create table clientes (
	id int primary key auto_increment, 
    nome varchar(50) not null,
    email varchar(100) not null,
    endereco longtext not null
);

create table produtos (
	id int primary key auto_increment, 
    nome varchar(50) not null,
    descricao longtext not null,
    preco float not null,
    quantidade_em_estoque int not null
);

create table pedidos (
	id int primary key auto_increment, 
    id_cliente int not null,
    data_pedido date not null,
	status_pedido varchar(50)
);

create table itens_pedido (
	id int primary key auto_increment,
    id_pedido int not null,
    id_produto int not null,
    quantidade int not null,
    preco_unitario float not null
);

insert into clientes (nome,email,endereco)
values ('Luan','luan@gmail.com','Rua Caliandra 255'),
('Luna','luna@gmail.com','Rua Bagda 391'),
('Elias','elias@gmail.com','Rua Itaparica 593'),
('Marcelina','marcelina@gmail.com','Rua SãoJoão 431');

insert into produtos (nome,descricao,preco,quantidade_em_estoque)
values ('Gatorade','bebida para hidratação do corpo',3.99,10),
('Coca-cola','refrigerante de cola',7.99,10),
('Arroz','produto alimenticio feito de trigo',19.99,10),
('Feijão','produto alimenticio feito de semente de feijão',9.99,10);

insert into pedidos (id_cliente,data_pedido,status_pedido)
values (1,20241209,'entregue'),
(2,20241002,'entregue'),
(3,20240226,'entregue'),
(4,20240428,'entregue');

insert into itens_pedido (id_pedido, id_produto, quantidade, preco_unitario)
values(1,2,1,7.99),
(2,4,3,9.99),
(3,3,2,19.99),
(4,1,3,3.99);

