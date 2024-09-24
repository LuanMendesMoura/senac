/*SELECIONAR E INSERIR INFORMAÇÕES NA TABELA ALUNOS*/
select * from `escola`.`alunos`;
insert into `escola`.`alunos`
(`nome`,`id_turma`,`nota`)
values('Felipe',5,8);

/*SELECIONAR E INSERIR INFORMAÇÕES NA TABELA TURMAS*/
select * from `escola`.`turmas`;
insert into `escola`.`turmas`
(`nome`)
values('Medicina');

/*SELECIONAR E INSERIR INFORMAÇÕES NA TABELA PROFESSORES*/
select * from `escola`.`professores`;
insert into `escola`.`professores`
(`nome`,`id_turma`)
values('Thiago',1),('Rafael',2);

/*SELECIONAR TODAS AS INFORMAÇÕES E COMPARAR A TABELA ALUNOS COM TURMAS*/
select * from `escola`.`alunos` as `alunos`
inner join `escola`.`turmas` as `turmas` on `turmas`.`id` = `alunos`.`id_turma`;

/*SELECIONAR ALGUMAS INFORMAÇÕES E COMPARAR A TABELA ALUNOS COM TURMAS*/
select `escola`.`alunos`.`id`, `escola`.`alunos`.`nome`, `escola`.`turmas`.`nome` as "turma", `escola`.`alunos`.`nota` from `escola`.`alunos`
inner join `escola`.`turmas` on `escola`.`turmas`.`id` = `escola`.`alunos`.`id_turma`;

/*SELECIONAR ALGUMAS INFORMAÇÕES E COMPARAR INFORMAÇÕES ESPECÍFICAS DA TABELA ALUNOS COM TURMAS*/
select * from `escola`.`alunos` as `alunos`
inner join `escola`.`turmas` as `turmas` on `turmas`.`id` = `alunos`.`id_turma`
where `alunos`.`nome` = 'Felipe' and `turmas`.`nome` = 'Medicina';

/*FORMA ABREVIADA PARA FAZER UM SELECT FROM*/
select `id`,`nome`,`id_turma`,`nota` from `escola`.`alunos`;

/*DELETAR TUPLAS*/
delete from `escola`.`alunos` where `id` in (6, 4);


select `escola`.`alunos`.`id`, `escola`.`alunos`.`nome`, `escola`.`turmas`.`nome` as "turma", `escola`.`alunos`.`nota`, `escola`.`professores`.`nome` as "nome professor" 
from `escola`.`alunos`
inner join `escola`.`turmas` on `escola`.`turmas`.`id` = `escola`.`alunos`.`id_turma`
inner join `escola`.`professores` on `escola`.`professores`.`id_turma` = `escola`.`turmas`.`id`

