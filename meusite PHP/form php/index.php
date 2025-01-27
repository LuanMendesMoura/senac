<?php
$nome = "Luan";
var_dump($nome);
echo "<br>";

$idade = 16;
var_dump($idade);
echo "<br>";


$float = 1.65;
var_dump($float);
echo "<br>";


$boolen = TRUE; // FALSE
var_dump($boolen);
echo "<br>";

$anoAtual = 2024;
$anoNascimento = 2007;
$idade = $anoAtual - $anoNascimento

?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,   initial-scale=1.0">
    <title>Meu Site</title>

</head>
<body>
    <h1>Bem vindo ao meu site PHP, <?php echo $nome ?> !</h1>
    <p>Sua idade é de <?php echo $idade ?> !</p>
    <p>
        <a href="form.html">form</a>
    </p>
</body>
</html>