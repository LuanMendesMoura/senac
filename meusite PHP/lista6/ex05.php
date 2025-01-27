<form action="ex05.php" method="POST">
    <div>
        <input type="text" name="nome" placeholder="Nome*">
        <input type="text" name="nota1" placeholder="Primeira Nota*">
        <input type="text" name="nota2" placeholder="Segunda Nota*">
        <input type="text" name="nota3" placeholder="Terceira Nota*">
        <button>Calcular Média</button>
    </div>
    <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {

            $nome = $_POST["nome"];
            $nota1 = (int) $_POST["nota1"];
            $nota2 = (int) $_POST["nota2"];
            $nota3 = (int) $_POST["nota3"];

            $media = ($nota1 + $nota2 + $nota3) / 3;

            $media = number_format($media,1);   

            echo "
                <p>Aluno(a): $nome </p>
                <p>Média: $media </p>
            ";
        }
    ?>

</form>