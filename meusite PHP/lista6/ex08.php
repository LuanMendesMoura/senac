<form action="ex08.php" method="POST">
    <div>
        <input type="text" name="cotacaodolar" placeholder="Cotação do Dólar">
        <input type="text" name="dolarvalor" placeholder="Valor em Dólar">
        <button>Converter</button>
    </div>
    <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST" ) {

            $cotacao = (float) $_POST["cotacaodolar"];
            $dolar = (float) $_POST["dolarvalor"];

            $reais = $dolar * $cotacao;

            echo "
                <p>Valor em Dólar:</p>
                <p>US$ $dolar</p>
                <p>Valor em Reais:</p>
                <p>R$ $reais</p>

            ";
        }
    ?>
</form>