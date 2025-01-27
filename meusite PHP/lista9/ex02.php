<form action="ex02.php" method="POST">
    <div>
        <button>Listar</button>
    </div>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST" ) {

        $n1 = 100;   

        while ($n1>0) {
            echo "$n1<br>";
            $n1--;
            }

        }
    ?>

</form>