import tkinter as tk
import database as db
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def janela_lista_livros():
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

    def delete_registro():
        selected_item = tabela_produtos.selection()

        if selected_item:
            item = tabela_produtos.item(selected_item)

            livro_id = item["values"][0]

            db.delete_livro(livro_id)

    # icon_delete_img = Image.open("assets/delete01.png").resize((16, 16))
    # icon = ImageTk.PhotoImage(icon_delete_img)

    btn_delete = tk.Button(nova_janela, text="Deletar", command=lambda:delete_registro())
    btn_delete.pack(pady=10)

def janela_cadastra_livro():

    # Método que limpa input
    def limpa_campos():
        input_nome.delete(0, tk.END)
        input_preco.delete(0, tk.END)
        input_categoria.delete(0, tk.END)
        input_autor.delete(0, tk.END)

    # Método que salva produto nos banco e limpa os inputs
    def salva_livro():
        db.cadastrar_livro(
            input_nome.get(), 
            input_preco.get(), 
            input_categoria.get(), 
            input_autor.get()
        )

        limpa_campos()

    nova_janela = tk.Toplevel()
    nova_janela.title("Cadastro de Livros")
    nova_janela.geometry("400x600")

    # Label e Input do Nome
    label_nome = tk.Label(nova_janela, text="Nome")
    label_nome.pack(pady=0)

    input_nome = tk.Entry(nova_janela)
    input_nome.pack(pady=5)

    # Label e Input do Preço
    label_preco = tk.Label(nova_janela, text="Preço")
    label_preco.pack(pady=0)

    input_preco = tk.Entry(nova_janela)
    input_preco.pack(pady=5)

    # Label e Input da idCategoria
    label_categoria = tk.Label(nova_janela, text="Categoria")
    label_categoria.pack(pady=0)

    input_categoria = tk.Entry(nova_janela)
    input_categoria.pack(pady=5)

    # Label e Input do idAutor
    label_autor = tk.Label(nova_janela, text="Autor")
    label_autor.pack(pady=0)

    input_autor = tk.Entry(nova_janela)
    input_autor.pack(pady=5)

    # Botão que vai cadastrar o livro no DB
    btn_cadastra_livro = tk.Button(nova_janela, text="Cadastrar", command=lambda:salva_livro())
    
    btn_cadastra_livro.pack(pady=10)

def janela_deletar_livro():
    nova_janela = tk.Toplevel()
    nova_janela.title("Deletar Livro")
    nova_janela.geometry("400x600")

    # Label e Input do DELETE IdProduto
    label_idLivro = tk.Label(nova_janela, text="ID Livro")
    label_idLivro.pack(pady=0)

    input_idLivro = tk.Entry(nova_janela)
    input_idLivro.pack(pady=5)

    btn_detele_livro = tk.Button(nova_janela, text="Deletar", command=lambda:db.delete_livro(input_idLivro.get()))
    btn_detele_livro.pack(pady=10)

def tela_principal():
    root = tk.Tk()
    root.title("BIblioteca")
    root.geometry("600x600")

    btn_listagem_livros = tk.Button(root, text="Abrir Lista De Livros", command=janela_lista_livros)
    btn_listagem_livros.pack(pady=10)

    btn_janela_cadastra_livro = tk.Button(root, text="Cadastrar Livro", command=janela_cadastra_livro)
    btn_janela_cadastra_livro.pack(pady=10)

    root.mainloop()