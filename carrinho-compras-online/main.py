from classes import *
from menu import *
from funcoes import *

import colorama
from colorama import Fore
from colorama import Style


# Fore.GREEN + "This is the color of grass" + Style.RESET_ALL
colorama.init()

lista_produtos=[]
inicio(lista_produtos)
carrinho = []

def fluxo_principal():
    close = True
    while close:
        primeiro_menu()
        op = int(input(Fore.GREEN + "Insira uma opção: "+ Style.RESET_ALL))
        if op == 1:
            fluxo_cliente()
        elif op == 2:
            fluxo_adm()
        elif op == 0:
            close = False
        else:
            print(Fore.LIGHTRED_EX + "Opção não encontrada! " + Style.RESET_ALL)

def fluxo_cliente():
    close = True
    while close:
        menu_cliente()
        op = int(input(Fore.GREEN + "Insira uma opção: " + Style.RESET_ALL))
        if op == 1:
            ver_produtos(lista_produtos)
        elif op == 2:
            fluxo_cliente_op2()
        elif op == 0:
            close = False
        else:
            print(Fore.LIGHTRED_EX + "Opção não encontrada! " + Style.RESET_ALL)

def fluxo_cliente_op2():
        close = True
        while close:
            menu_carrinho()
            op = int(input(Fore.GREEN + "Insira uma opção: "+ Style.RESET_ALL))
            if op == 1:
                ver_produtos_carrinho(carrinho)
            elif op == 2:
                adicionar_produto_carrinho(lista_produtos,carrinho)
                sub_menu_adicionar_produto_carrinho()
                op = int(input(Fore.GREEN + "Insira uma opção: "+ Style.RESET_ALL))
                while op == 1:
                    adicionar_produto_carrinho(lista_produtos,carrinho)
                    sub_menu_adicionar_produto_carrinho()
                    op = int(input(Fore.GREEN + "Insira uma opção: "+ Style.RESET_ALL))
                if op == 0:
                    close = False
            elif op == 3:
                remover_produto_carrinho(carrinho)
            elif op == 0:
                close = False
            else:
                print(Fore.LIGHTRED_EX + "Opção não encontrada! " + Style.RESET_ALL)

def fluxo_adm():
    close = True
    while close: 
        menu_adm()
        op = int(input(Fore.GREEN + "Insira uma opção: "+ Style.RESET_ALL))     
        if op == 1:
            adicionar_produto(lista_produtos)  
        elif op == 2:
            editar_produto(lista_produtos)
        elif op == 3:
            excluir_produto(lista_produtos)
        elif op == 4:
            ver_produtos(lista_produtos)
        elif op == 0:
            close = False

fluxo_principal()
