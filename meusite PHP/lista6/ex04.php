<form action="ex04.php" method="POST">
    <div>
        <input type="text" name="nome" placeholder="Nome*">
        <input type="text" name="salario" placeholder="Salário*">
        <input type="text" name="vendas" placeholder="Vendas (em dinheiro)*">
        <button>Calcular</button>
    </div>
    <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {

            $nome = $_POST["nome"];
            $salarioFixo = (int) $_POST["salario"];
            $vendas = (int) $_POST["vendas"];

            $salarioFinal = $salarioFixo + (0.15*$vendas);

            echo "
                <p>Nome: $nome</p>
                <p>Salário Fixo: $salarioFixo</p>
                <p>Salário Final: $salarioFinal</p>

            ";
        }
    ?>
</form>