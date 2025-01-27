/* CRIARMOS UM METODO (FUNCAO) DO MYSQL */

DELIMITER //

CREATE PROCEDURE a_vista_preco(in taxa_a_vista int, in id_livro int)
BEGIN

	UPDATE livros 
    SET preco = preco - (preco * (taxa_a_vista/100))
    WHERE id = id_livro;

	select	* from livros;

END //
DELIMITER;

/* CHAMAR A PROCEDURE */
call a_vista_preco(10,8);
/* APAGAR A PROCEDURE (METODO) */
drop procedure if exists a_vista_preco;

DELIMITER //

CREATE PROCEDURE excluir_livro(in id_livro int)
BEGIN
	SET FOREIGN_KEY_CHECKS=0;
	DELETE FROM livros WHERE id = id_livro;
END //
DELIMITER;

call excluir_livro(1);

DELIMITER //

CREATE PROCEDURE nova_data_compra_carrinho(in nova_data_compra date, in id_carrinho int)
BEGIN

	UPDATE carrinhos 
    SET data_compra = nova_data_compra
    WHERE id = id_carrinho;

	select	* from carrinhos;

END //
DELIMITER;

call nova_data_compra_carrinho("2024-01-20",1)