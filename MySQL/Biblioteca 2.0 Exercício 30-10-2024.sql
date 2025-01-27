drop database biblioteca;
create database biblioteca;
use biblioteca;

create table autores (
	id int primary key auto_increment,
    nome varchar(50) not null
);

create table categorias (
	id int primary key auto_increment,
    nome_categoria varchar(50) not null
);

create table livros (
	id int primary key auto_increment,
    nome varchar(50) not null,
    preco decimal (10,2) not null,
    id_categoria int not null,
    id_autor int not null,
    foreign key (id_categoria) references categorias(id),
    foreign key (id_autor) references autores(id)
);

create table clientes (
	id int auto_increment unique not null,
    cpf varchar(14) primary key,
    nome varchar(50) not null,
    email varchar(100) not null,
    telefone varchar(20) not null
);

create table carrinhos (
	id int primary key auto_increment,
    data_compra date not null,
    id_livro int not null,
    cpf_cliente varchar(14) not null,
    valor_total decimal(10,2) not null,
    foreign key (id_livro) references livros(id),
    foreign key (cpf_cliente) references clientes(cpf)
);


insert into autores (nome)
values 
('Mauricio de Sousa'),
('Jeff Kinney'),
('Stephenie Meyer'),
(' William P. Young'),
('George Orwell'),
('Machado de Assis'),
('J.K. Rowling'),
('Gabriel García Márquez'),
('Jane Austen'),
('F. Scott Fitzgerald'),
('Herman Melville'),
('Agatha Christie'),
('Chimamanda Ngozi Adichie');

insert into categorias (nome_categoria)
values 
('Suspense'),
('Drama'),
('Romance'),
('Diário'),
('HQ'),
('Ficção Científica'),
('Fantasia'),
('Mistério'),
('Biografia'),
('Não Ficção'),
('Terror'),
('Aventura'),
('Literatura Infantojuvenil');

insert into livros (nome,preco,id_categoria,id_autor)
values 
('Crepúsculo',20.99,3,3),
('Diário de um Banana',20.99,4,2),
('Turma da Mônica Jovem',20.99,5,1),
('A Cabana',20.99,1,4),
('O Alquimista', 25.50, 2, 4),
('1984', 15.75, 3, 2),
('A Revolução dos Bichos', 12.30, 4, 3),
('Dom Casmurro', 10.00, 3, 5),
('O Pequeno Príncipe', 20.00, 5, 4),
('A Metamorfose', 18.75, 2, 3),
('Cem Anos de Solidão', 25.00, 4, 5),
('Moby Dick', 17.80, 2, 3),
('A Menina que Roubava Livros', 19.90, 5, 4),
('O Senhor dos Anéis', 30.00, 1, 5);

insert into clientes (cpf,nome,email,telefone)
values 
('111.111.111-11', 'Luan', 'luan@gmail.com', '(67)993223251'),
('222.222.222-22', 'Maria', 'maria@gmail.com', '(67)998877665'),
('333.333.333-33', 'Carlos', 'carlos@gmail.com', '(67)987654321'),
('444.444.444-44', 'Ana', 'ana@gmail.com', '(67)976543210'),
('555.555.555-55', 'Joaquim', 'joaquim@gmail.com', '(67)965432109'),
('123.456.789-01', 'Maria', 'maria@gmail.com', '(67)91234-5678'),
('234.567.890-12', 'Carlos', 'carlos@gmail.com', '(67)93456-7890'),
('345.678.901-23', 'Ana', 'ana@gmail.com', '(67)94567-8901'),
('456.789.012-34', 'Pedro', 'pedro@gmail.com', '(67)95678-9012'),
('567.890.123-45', 'Julia', 'julia@gmail.com', '(67)96789-0123'),
('678.901.234-56', 'Ricardo', 'ricardo@gmail.com', '(67)97890-1234'),
('789.012.345-67', 'Fernanda', 'fernanda@gmail.com', '(67)98901-2345'),
('890.123.456-78', 'Lucas', 'lucas@gmail.com', '(67)99012-3456'),
('901.234.567-89', 'Roberta', 'roberta@gmail.com', '(67)99234-5678'),
('012.345.678-90', 'Gabriel', 'gabriel@gmail.com', '(67)99456-7890');

insert into carrinhos (data_compra, id_livro, cpf_cliente, valor_total)
values 
('2024-10-30', 1, '111.111.111-11', 88.9),
('2024-11-01', 2, '345.678.901-23', 75.5),
('2024-12-15', 1, '222.222.222-22', 90.0),
('2025-01-20', 3, '456.789.012-34', 82.3),
('2024-11-05', 4, '123.456.789-01', 67.8),
('2024-09-10', 2, '567.890.123-45', 85.0),
('2024-11-15', 3, '333.333.333-33', 72.4),
('2024-12-01', 7, '678.901.234-56', 95.6),
('2024-04-10', 5, '444.444.444-44', 60.0),
('2024-12-20', 2, '789.012.345-67', 78.9),
('2024-01-05', 7, '555.555.555-55', 88.1),
('2024-01-15', 6, '890.123.456-78', 92.3),
('2024-03-25', 3, '234.567.890-12', 81.4),
('2024-02-10', 2, '901.234.567-89', 76.2);

select l.id, l.nome, l.preco, c.nome_categoria, a.nome from livros as l
inner join categorias as c
on c.id = l.id_categoria
inner join autores as a
on a.id = l.id_autor;

select c.id, c.data_compra, l.nome, cl.nome, c.valor_total from carrinhos as c
inner join livros as l
on l.id = c.id_livro
inner join clientes as cl
on cl.cpf = c.cpf_cliente;

select * from livros where nome LIKE '%turma%';
 



 