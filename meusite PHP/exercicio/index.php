<?php

// IF .. ELSE
$num1 = 11;

// par ou impar
//  condição
if ( ($num1 % 2) == 0 ) {
    // executa este bloco se a condição
    // for TRUE
    echo "$num1 é PAR!";
} else {
    // executa este bloco se a condição
    // for FALSE
    echo "$num1 é IMPAR!";
}
echo "<br><br>";

// IF .. ELSE IF
$num1 = 3;
$num2 = 3;

if ($num1 < $num2) {
    echo "$num1 MENOR que $num2";
} else if ($num1 > $num2) {
    echo "$num1 MAIOR que $num2";
} else {
    echo "$num1 IGUAL a $num2";
}

echo "<br><br>";

// Ternário

$idade = 10;

$mensagem = $idade >= 18 
    ? "MAIOR DE IDADE" 
    : "MENOR DE IDADE";

echo $mensagem;

echo "<br><br>";

// Funções
function olaMundo() {
    echo "Olá Mundo";
}

function olaPessoa($nome) {
    echo "Olá $nome";
}

function soma($a, $b) {
    return $a + $b;
}


?>

<h1> <?php olaMundo() ?> </h1>
<h1> <?php olaPessoa("Thiago") ?> </h1>
<p> <?php echo soma(10, 5) ?> </p>