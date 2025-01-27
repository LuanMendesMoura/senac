<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EX03</title>
</head>
<body>
    <form action="ex03.php" method="POST">
        <div>
            <p>Ex03: Consumo Médio</p>
            <input type="text" name="distancia">
            <input type="text" name="combustivel">
            <button>Calcular</button>
        </div>
        <?php
            if ($_SERVER["REQUEST_METHOD"] == "POST") {
                $distancia = (int) $_POST["distancia"];
                $combustivel = (int) $_POST["combustivel"];

                $consumoMedio = $distancia/$combustivel;

                echo "
                    <p>Consumo Médio: $consumoMedio </p>
                ";
            }
        ?>
    </form>
</body>
</html>