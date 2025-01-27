<form action="exercicios.php" method="POST">
    <div>
        <p>Ex 1 e 2 - Calculadora</p>
        <input type="text" name="a">
        <input type="text" name="b">
        <button>Calcular</button>
    </div>
    <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $a = (int) $_POST["a"];
            $b = (int) $_POST["b"];
            
            $soma = $a + $b;
            $sub = $a - $b;
            $mult = $a * $b;
            $div = $a / $b;

            echo "
                <p>Operações entre $a e $b</p>
                <p>Soma: $soma</p>
                <p>Sub: $sub</p>
                <p>Mult: $mult</p>
                <p>Div: $div</p>
            ";
        }
    ?>
</form>

