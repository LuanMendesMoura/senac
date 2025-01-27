<form action="ex06.php" method="POST">
    <div>
        <input type="text" name="n1" placeholder="Digite um número">
        <button>Calcular</button>
    </div>
    <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST" ) {

            $n1 = (int) $_POST ["n1"];
            
            if ($n1 >= 0) {

                $raiz = $n1 ** 0.5;
                $raiz = number_format($raiz,2);

                echo "
                    <p>A raiz de $n1 é $raiz</p>
                ";

            } else {

                $quadrado = $n1 ** 2;

                echo "
                    <p>O quadrado de $n1 é $quadrado</p>
                ";
            }
        } 
    ?>
</form>