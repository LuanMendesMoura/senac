<form action="ex08.php" method="POST">
    <div>
        <input type="text" name="n1" placeholder="Digite um número*">
        <button>Divisível</button>
    </div>

    <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST" ) {

            $n1 = (int) $_POST["n1"];

            if (($n1 % 5) == 0) {
                echo "
                    <p>O número $n1 é divisível por 5</p>
                ";
            }
            else {
                echo "
                    <p>O número $n1 não é divisível por 5</p>
                ";
            }
        }
    ?>
</form>