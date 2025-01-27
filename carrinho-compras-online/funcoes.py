from classes import *

def inicio(lista_produtos):
    produto=Produto("Arroz",27.99,50)
    lista_produtos.append(produto)

    produto=Produto("Feijão",7.99,50)
    lista_produtos.append(produto)

    produto=Produto("Macarrão",5.99,50)
    lista_produtos.append(produto)

    produto=Produto("Ovo",12.99,50)
    lista_produtos.append(produto)

    produto=Produto("Leite",5.99,50)
    lista_produtos.append(produto)
    
def adicionar_produto(lista_produtos):
    nome = input("Digite o nome do produto: ")
    for item in lista_produtos:
        if item.nome == nome:
            while item.nome == nome:
                print("Produto já cadastrado!")
                nome = input("Digite o nome do produto: ")
                
    preco = input("Digite o preço do produto: ")
    quantidade = input("Digite a quantidade do produto: ")
    

    produto = Produto(nome,preco,quantidade)
    lista_produtos.append(produto)

def ver_produtos(lista_produtos):
    print("\n----- PRODUTOS ------")
    for index,item in zip(range(0,len(lista_produtos)),lista_produtos):
        print(f"\nCÓDIGO: {index} - Nome: {item.nome}")
        print(f"            Valor: {item.preco}")
        print(f"            Quantidade: {item.quantidade}")

def excluir_produto(lista_produtos):
    codigo = int(input("Digite o código do produto que deseja remover: "))
    lista_produtos.pop(codigo)
    # if codigo != lista_produtos:
    #     print("Código não encontrado! ")

def editar_produto(lista_produto):
    codigo = int(input("Digite o código do produto que deseja editar: "))  
    print(f"Editar Produto CÓDIGO: {codigo}")
    nome = input(f"Novo nome do produto: ")
    preco = input(f"Novo preço do produto: ")
    quantidade = input(f"Nova quantidade do produto: ")
    lista_produto[codigo].nome = nome
    lista_produto[codigo].preco = preco
    lista_produto[codigo].quantidade = quantidade


def adicionar_produto_carrinho(lista_produtos,carrinho):
        nome = input("Digite o nome do produto: ")
        for item in lista_produtos:
            if item.nome == nome:
                quantidade = int(input("Digite a quantidade do produto: "))
                item.quantidade = item.quantidade - quantidade
                produto = Carrinho(nome,item.preco,quantidade)            
                carrinho.append(produto)
                
def remover_produto_carrinho(carrinho):
    codigo = int(input("Digite o código do produto que deseja remover: "))
    carrinho.pop(codigo)
    # if codigo != carrinho:
    #     print("Código não encontrado! ")

def ver_produtos_carrinho(carrinho):
    print("\n----- MEU CARRINHO ------")
    for index,item in zip(range(0,len(carrinho)),carrinho):
        print(f"\nCÓDIGO: {index} - Nome: {item.nome}")
        print(f"            Valor: {item.preco}")
        print(f"            Quantidade: {item.quantidade}")

           