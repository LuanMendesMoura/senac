import funcoes as f 
import views as v
catalogo = []
sair = True 
while sair:
    v.menu_principal()
    opcao = int(input("INFORME UMA OPÇÃO: "))
    if opcao == 1:
        for i in range(0,6):
            print(f"SAINDO {i}")
        sair = False
    elif opcao == 2:
        print(f"{10*"-"}MENU ONG{10*"-"}")
        nome = input("NOME DA ONG: ")
        tipo = input("TIPO DA ONG: ")
        cnpj = input("CNPJ DA ONG: ")
        ong = f.create_ong(nome,tipo,cnpj)
        catalogo.append(ong)
    elif opcao == 3: 
        print(f"{10*"-"}PROJETO{10*"-"}\n")
        nome = input("CRIE UM PROJETO: ")
        descricao = input("DESCRIÇÃO: ")
        projeto = f.create_projeto(nome,descricao)
        nome_ong = input("DIGITE O NOME DA ONG: ")
        index = f.localiza_ong_index(nome_ong, catalogo)
        if index is None:
            print("NÃO EXISTE!! ")
            break
        catalogo[index]["projeto"].append(projeto)
        ong['projeto'].append(projeto)
    elif opcao == 4:
        nome_ong = input("NOME DA ONG: ")
        index = f.localiza_ong_index(nome_ong, catalogo)
        if index is None:
            print("ONG NÃO ENCONTRADA!! ")
        catalogo[index]["nome"] = input("NOVO NOME: ")
        