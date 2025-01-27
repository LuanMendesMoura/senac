<form action="ex07.php" method="POST">
    <div>
        <input type="text" name="Celsius" placeholder="Graus Celsius">
        <button>Converter</button>
    </div>
    <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST" ) {

            $celsius = (int) $_POST["Celsius"];
            $fahrenheit = (9*$celsius+160)/5;

            echo "
                <p>Temperatura</p>
                <p>Celsius: $celsius</p>
                <p>Fahrenheit: $fahrenheit</p>
            ";
        }
    ?>
</form>