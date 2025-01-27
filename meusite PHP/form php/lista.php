<?php

// array indexado
$produtos = ["Mouse","Teclado","Monitor","MousePad",1,9];

// var_dump($produtos);
echo "<br>";

// echo $produtos[0];
echo "<br>";

$produtos[2] = "Mouse";
// var_dump($produtos);
echo "<br>";
echo "<br>";


// array associativo
$produtos2 = [
    "nome" => "Computador",
    "preco" => 1999
];
// var_dump($produtos2);
// echo "<br>";

// echo $produtos2["nome"];
echo "<br>";
// echo $produtos2["preco"];
echo "<br>";
echo "<br>";

// array multidimensional
$produtos3 = [
    [
        "nome" => "Computador",
        "preco" => 1999
    ],
    [
        "nome" => "Teclado",
        "preco" => 150
    ],
    [
        "nome" => "Mouse",
        "preco" => 200
    ],
    [
        "nome" => "Monitor",
        "preco" => 997.90
    ]
];
echo "<pre>";
// print_r($produtos3);
echo "</pre>";
?>

<ul>
    <li>
        Nome: <?php echo $produtos3[0]["nome"]?>
        <br>
        Preço: <?php echo $produtos3[0]["preco"]?>
    </li>
    <br>
    <li>
        Nome: <?php echo $produtos3[1]["nome"]?>
        <br>
        Preço: <?php echo $produtos3[1]["preco"]?>
    </li>
    <br>
    <li>
        Nome: <?php echo $produtos3[2]["nome"]?>
        <br>
        Preço: <?php echo $produtos3[2]["preco"]?>
    </li>
    <br>
    <li>
        Nome: <?php echo $produtos3[3]["nome"]?>
        <br>
        Preço: <?php echo $produtos3[3]["preco"]?>
    </li>
</ul>