<form action="ex04.php" method="POST">
    <div>
        <button>Listar</button>
    </div>
    <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST" ) {
            $i = 200;
            while ($i > 99) {
                echo "$i<br>";
                $i--;
            }
        }
    ?>
</form>