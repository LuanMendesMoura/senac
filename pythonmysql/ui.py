import tkinter as tk
import database as db
from tkinter import ttk

def listagem_livros():
    nova_janela = tk.Toplevel()
    nova_janela.title("Listagem de livros")
    nova_janela.geometry("600x600")

    label_titulo = tk.Label(nova_janela, text="Listagem de livros")
    label_titulo.pack(pady=10)

    colunas = ("ID", "Nome", "Preço")
    tabela_produtos = ttk.Treeview(nova_janela, columns=colunas, show="headings")
    tabela_produtos.pack(fill="both")

    #CONFIGURA O CABEÇALHO DA COLUNA
    tabela_produtos.heading("ID", text="ID")
    tabela_produtos.heading("Nome", text="Nome")
    tabela_produtos.heading("Preço", text="Preço")

    #ESPECIFICAR TAMANHO DA COLUNA
    
    tabela_produtos.column("ID", width=50)
    tabela_produtos.column("Nome", width=150)
    tabela_produtos.column("Preço", width=100)

    btn_lista_produtos = tk.Button(nova_janela, text="Listar Produtos", command=lambda:carregar_produtos())
    btn_lista_produtos.pack(pady=10)


    def carregar_produtos():
        registros = db.buscar_todos("livros")

        for item in tabela_produtos.get_children():
            tabela_produtos.delete(item)

        for registro in registros:
            tabela_produtos.insert("", tk.END, values=registro)



    # btn_fechar = tk.Button(nova_janela, text="Fechar", command=nova_janela.destroy)
    # btn_fechar.pack(pady=10)

def tela_principal():
    root = tk.Tk()
    root.title("BIblioteca")
    root.geometry("600x600")

    # tk.Button(root, text="IMPRIMIR LIVROS", width=30, command=lambda: db.buscar_todos('livros')).pack(pady=10)

    # tk.Label(root, text="NOME DO LIVRO", width=50).pack()
    
    # input_livro = tk.Entry(root)
    # input_livro.pack()


    def atualizar_registro():
        registros = db.buscar_todos("livros")
        registros_texto.config(text=registros)

    btn_listar_todos = tk.Button(root, text="Listar Todos", command=lambda: atualizar_registro())
    btn_listar_todos.pack(pady=10)

    btn_listagem_livros = tk.Button(root, text="Abrir lista de livros", command=listagem_livros)
    btn_listagem_livros.pack(pady=10)

    #LABEL QUE MOSTRA TODOS OS MEUS PRODUTOS
    registros_texto = tk.Label(root, text="", justify="left", anchor="center")
    registros_texto.pack(pady=10)

    root.mainloop()