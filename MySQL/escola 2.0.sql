use escola;

select a.id, a.nome, a.nota, t.nome as disciplina, p.nome as professor from alunos as a
inner join turmas as t on t.id = a.id_turma
inner join professores as p on p.id_turma = a.id_turma;

select * from professores;

update alunos
set id_turma = 2
where id = 13;

create table pediodos (
	id int primary key unique auto_increment not null,
    periodo varchar(20) not null
);

insert into periodos (periodo) 
values ('Matutino'),('Vespertino'),('Noturno'),('Integral');

select * from turmas;

ALTER TABLE `escola`.`alunos` 
ADD COLUMN `id_periodo` INT NOT NULL 
AFTER `nota`;

update turmas
set nome = 'Gestão de Projetos'
where id = 3; 

select a.id, a.nome, a.nota, t.nome as disciplina, p.nome as professor, pe.periodo
from alunos as a
inner join turmas as t on t.id = a.id_turma
inner join professores as p on p.id_turma = a.id_turma
inner join periodos as pe on pe.id = a.id_periodo;	

