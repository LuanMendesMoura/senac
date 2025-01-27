<?php
    $nome = $_POST["nome"];
    $descricao = $_POST["descricao"];
    $preco = (float) $_POST["preco"];

    if ($preco < 10){
        echo '<h1 style="color: red;">Produto inválido!</h1>';
        exit;
    }

?>

<div>
    <h1>Cadastrado com sucesso!</h1>

    <p>Nome do produto: <?php echo $nome ?></p>
    <p>Preço: <?php echo $preco ?></p>
    <p>Descrição: <?php echo $descricao ?></p>

    <p> 
        <a href="lista.php">Lista</a>
    </p>
</div>