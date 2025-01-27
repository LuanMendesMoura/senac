<form action="ex01.php" method="POST">
    <div>
        <p>Informe um número</p>
        <input type="text" name="n1" placeholder="Digite um número*">
        <button>Enviar</button>
    </div>
    <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            
            $n1 = (int) $_POST["n1"];

            if ($n1 > 20) {

                echo "
                    <p>O número $n1 é maior que 20!</p>
                ";
            } else {
                echo "
                    <p>O número $n1 é menor que 20!</p>
                ";
            }
        }
    ?>
</form>