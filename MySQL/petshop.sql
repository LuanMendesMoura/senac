create database petshop;
use petshop;

create table clientes (
	id int primary key auto_increment,
	nome varchar(50),
    dt_nascimento date,
    cpf varchar(14) unique,
	logradouro varchar(50),
    bairro varchar(25),
    numero varchar(4),
    complemento varchar(15),
    telefone varchar(14)
);

create table animais (
	id int primary key auto_increment,
    nome varchar(50),
    idade int,
    raca varchar(30),
    tipo_especie int,
    id_cliente int
);

create table especies (
	id int primary key auto_increment,
    especie varchar(35)
);

create table servicos (
	id int primary key auto_increment,
    descricao varchar(35),
    valor float
);

create table atendimentos (
	id int primary key auto_increment,
    dt_atendimento date,
    id_servico int,
    id_animal int
);

create table profissionais (
	id int primary key auto_increment,
    nome varchar(50),
    telefone varchar(15),
    crmv varchar(9) unique
);

/*---------------------------------------------------------------------------------------*/

insert into clientes(nome, dt_nascimento, cpf, logradouro, bairro, numero, complemento,telefone)
values('Luan','2007-12-09','71370074140','R. Bagda','Trevisso','381','','67993223251'),
('Pedro','2008-09-17','98780767878','R. Maringá','Honduras','391','','67998878099'),
('Miguel','2008-09-17','98780767876','R. Maringá','Honduras','391','','67998878097');

insert into especies(especie)
values('Cachorro'),('Gato'),('Coelho'),('Peixe'),('Passaro');

insert into animais(nome, idade, raca, tipo_especie, id_cliente)
values('Magali',3,'Vira-lata',1,1),('Pandora',1,'Vira-lata',1,1),
('Kent',2,'Poodle',1,3),('Duke',1,'Palhaço',4,2);

insert into servicos (descricao,valor)
values('Banho',60.00),('Tosa',60.00),('Banho e Tosa',110.00),
('Vacinação',80.00),('Spa',200.00);

insert into atendimentos (dt_atendimento, id_servico, id_animal)
values ('2024-10-10',3,2);

insert into profissionais (nome,telefone,crmv)
values('Arnold','67998322313','000000001'),
('Carlos','67998322314','000000002'),
('Felipe','67998322315','000000003');

/*---------------------------------------------------------------------------------------*/

alter table clientes add column complemento varchar(15) after numero;
alter table atendimentos add column id_profissional int;

update clientes set complemento = '' where id = 1;
update atendimentos set id_profissional = 3 where id = 3 ;

select * from clientes;
select * from animais;
select * from especies;
select * from servicos;
select * from atendimentos;

select c.nome as cliente, c.logradouro, c.bairro, c.numero, a.nome as pet, e.especie from clientes as c 
inner join animais as a
on c.id = a.id_cliente 
inner join especies as e
on e.id = a.tipo_especie;

select an.nome as pet, e.especie, a.dt_atendimento, s.descricao, s.valor, c.nome as dono, p.nome as veterinario
from atendimentos as a
inner join servicos as s
on s.id = a.id_servico 
inner join animais as an 
on an.id = a.id_animal
inner join clientes as c
on an.id_cliente = c.id
inner join especies as e
on e.id = an.tipo_especie
inner join profissionais as p
on p.id = a.id_profissional;