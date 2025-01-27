set @total = 0.0;

select @total := SUM(preco)
from livros;

select @total as total;

-- AVG

set @media_preco = 0;

select @media_preco := AVG(preco)
from livros;

select @media_preco media_preco;

select distinct id, nome from clientes;