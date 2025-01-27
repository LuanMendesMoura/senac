import colorama
from colorama import Fore
from colorama import Style


# Fore.GREEN + "This is the color of grass" + Style.RESET_ALL
colorama.init()



def primeiro_menu():
    print(Fore.CYAN + """\n----- LOGIN ------
1 - Cliente\n2 - Administrador\n0 - Sair\n""" + Style.RESET_ALL)

def menu_adm():
    print(Fore.CYAN + """\n----- OLÁ ADMINISTRADOR ------
1 - Adicionar produto\n2 - Editar produto\n3 - Excluir produto\n4 - Ver produtos\n0 - Voltar\n""" + Style.RESET_ALL)

def menu_cliente():
    print(Fore.CYAN + """\n----- OLÁ CLIENTE ------
1 - Ver produtos\n2 - Meu carrinho\n0 - Voltar\n""" + Style.RESET_ALL)

def menu_carrinho():
    print(Fore.CYAN + """\n----- OPÇÕES CARRINHO ------
1 - Ver carrinho\n2 - Adicionar produtos\n3 - Remover produtos\n0 - Voltar\n""" + Style.RESET_ALL)
    
def sub_menu_adicionar_produto_carrinho():
    print(Fore.CYAN + """\n----- OPÇÕES ------
1 - Adicionar mais produtos\n0 - Voltar\n""" + Style.RESET_ALL)