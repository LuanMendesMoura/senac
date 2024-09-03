from menus import *
from views import *
from login import *
from crud import *

def fluxo_principal():
    close = True
    clear_flag=True
    while close:
        print(menu_principal(limpar=clear_flag))        
        op = input("Escolha uma opção: ")
        if op == '1': 
            token = login()
            if token != None:
               fluxo_logado(token)
               clear_flag=True 
            else:
                clear_flag=False
                print("Erro no login!")
        elif op == '2':
            result = create_login()
            if result ==True:
                print("Usuário Criado!")
            else:
                clear_flag=False
                print("Erro na Criação!")
        elif op == '3':
            ongs=getOngs()
            view_ongs(ongs)
            clear_flag=False
        elif op == '0':
            close=False
        else:
            print("Opção Inválida")

    
def fluxo_logado(token):
    close = True
    while close:       
        print(menu_principal(True))
        op = input("Escolha uma opção: ")
        if op == '1': 
           ongs=getOngs()
           view_ongs(ongs)
           index_ong = int(input("Informe [index]:"))
           fluxo_ong(ongs[index_ong],token)
        elif op == '2':           
            createOng(token)
        elif op == '0': 
           close = False
        else:
            print("Opção Inválida")


def fluxo_ong(ong:ONG, token):
    close = True
    while close: 
        print(menu_ong())
        op = input("Escolha uma opção: ")
        if op == '1': 
            fluxo_editar_ong(ong)
        elif op == '2': 
            fluxo_projeto(ong)
        elif op == '3': 
            api_update(ong,token)
        elif op == '4': 
            confirma = input("1 - SIM\n2 - NÃO\nEscolha uma opção: ")
            if confirma == '1':
                api_delete(ong,token)
            elif confirma == '2':
                pass
        elif op == '0': 
           close = False
        else:
            print("Opção Inválida")



def fluxo_editar_ong(ong:ONG):
    close = True
    while close: 
        print(ong.getNome())
        ong.setNome(input("Digite novo nome: "))
        print(ong.to_json())
        close=False
    

def fluxo_projeto(ong:ONG):
    close = True
    while close: 
        projetos=ong.getProjetos()
        view_projetos(projetos)
        print("-1 - Sair")
        op = int(input("Digite [index]: "))
        if op > -1 and op < len(projetos):
            print(projetos[op].getNome())
            fluxo_editar_projeto(projetos[op])
        elif op == -1:
             close=False
        else:
            print("Index Inválido")



def fluxo_editar_projeto(projeto:Projeto):
    close = True
    while close: 
        print(projeto.to_json())
        print(menu_editar_projeto())
        op = input("opção: ")
        if op == '1':
            projeto.setNome(input("Digite novo nome: "))
        elif op == '2':
            projeto.setDescricao(input("Digite nova Descricão: "))
        elif op == '3':
            projeto.setResposavel(input("Digite novo Responsavel: "))
        elif op == '4':
            projeto.setStatus(input("Digite novo Status: "))
        elif op == '0':
            close=False
        else:
            print("Opção Inválida")


fluxo_principal()
