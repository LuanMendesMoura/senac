create database DadosPessoais;
use dadospessoais;

create table pessoas (
	id int primary key auto_increment not null,
    nome varchar(50) not null,
    id_telefone int not null,
    id_cpf int not null,
    id_data_nascimento int not null
);

create table telefone (
	id int primary key auto_increment not null,
    id_pessoa int not null,
    telefone int8 not null
);

create table cpf (
	id int primary key auto_increment not null,
    id_pessoa int not null,
    cpf varchar(14) not null
);

create table data_nascimento (
	id int primary key auto_increment not null,
    id_pessoa int not null,
    data_nascimento date not null
);

insert into pessoas (nome,id_telefone,id_cpf,id_data_nascimento) values ('Luan',1,1,1);

insert into telefone (id_pessoa,telefone) values (1,67993223251);

insert into cpf (id_pessoa,cpf) values (1,'71370074140');

insert into data_nascimento (id_pessoa,data_nascimento) values (1,'2007-12-09');

select p.id, p.nome, cpf.cpf, dn.data_nascimento, t.telefone from pessoas as p
inner join cpf on cpf.id = p.id_cpf
inner join data_nascimento as dn on dn.id = p.id_data_nascimento
inner join telefone as t on t.id = p.id_telefone
