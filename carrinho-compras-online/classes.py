class Usuário():
    login:str
    senha:str
    def __init__(self, login, senha):
        self.login=login
        self.senha=senha

class Produto():
    nome:str
    preco:float
    quantidade:int
    def __init__(self,nome,preco,quantidade):
        self.nome=nome
        self.preco=preco
        self.quantidade=quantidade

class Carrinho(Produto):
    def __init__(self, nome, preco, quantidade):
        super().__init__(nome, preco, quantidade)

