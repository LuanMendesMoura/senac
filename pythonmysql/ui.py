import tkinter as tk
import database as db
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def janela_lista_livros():
    nova_janela = tk.Toplevel()
    nova_janela.title("Listagem de livros")
    nova_janela.geometry("600x600")

    # TITULO DA MINHA JANELA
    label_titulo = tk.Label(nova_janela, text="Listagem de livros")
    label_titulo.pack(pady=10)

    def aplicar_filtro():
        for item in tabela_produtos.get_children():
            tabela_produtos.delete(item)

        registros_filtro = db.buscar_livro_nome(entry_nome.get())

        for registro in registros_filtro:
            tabela_produtos.insert("", "end", values=(
                registro.get("id", ""),
                registro.get("nome", ""),
                registro.get("preco", ""),
            ))

    # LABEL PARA PROCURAR LIVRO
    tk.Label(nova_janela, text="Procurar").pack(pady=10)
    # INPUT - CAIXA DE PERGUNTA
    entry_nome = tk.Entry(nova_janela, width=50)
    entry_nome.pack(pady=10)
    # BTN PARA PROCURAR
    btn_filtro = tk.Button(nova_janela, text="Filtrar", command=lambda:aplicar_filtro())
    btn_filtro.pack(pady=10)
    
    colunas = ("ID", "Nome", "Preço")
    tabela_produtos = ttk.Treeview(nova_janela, columns=colunas, show="headings")
    tabela_produtos.pack(fill="both")

    # CONFIGURA O CABEÇALHO DA COLUNA
    tabela_produtos.heading("ID", text="ID")
    tabela_produtos.heading("Nome", text="Nome")
    tabela_produtos.heading("Preço", text="Preço")

    # ESPECIFICAR TAMANHO DA COLUNA
    tabela_produtos.column("ID", width=50)
    tabela_produtos.column("Nome", width=150)
    tabela_produtos.column("Preço", width=100)

    # BOTÕES
    btn_listar_livros = tk.Button(nova_janela, text="Listar Produtos", command=lambda:listar_registros())
    btn_listar_livros.pack(pady=10)

    btn_editar_livro = tk.Button(nova_janela, text="Editar", command=lambda:editar_registro())
    btn_editar_livro.pack(pady=10)

    btn_delete_livro = tk.Button(nova_janela, text="Deletar", command=lambda:delete_registro())
    btn_delete_livro.pack(pady=10)

    def listar_registros():
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

            nova_janela.destroy()

    def editar_registro():
        selected_item = tabela_produtos.selection()

        if selected_item:
            item = tabela_produtos.item(selected_item)

            livro_id = item["values"][0]

            janela_editar_registro(livro_id)

            nova_janela.destroy()

def janela_cadastra_livro():
    nova_janela = tk.Toplevel()
    nova_janela.title("Cadastro de Livros")
    nova_janela.geometry("400x600")

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

    # Label e Input do Nome
    tk.Label(nova_janela, text="Nome").pack(pady=0)

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

def janela_editar_registro(livro_id):
    lancamentos = db.buscar_produto_id(livro_id)

    nova_janela = tk.Toplevel()
    nova_janela.title("Editar Livro")
    nova_janela.geometry("600x600")

    tk.Label(nova_janela, text="ID DO LIVRO").pack(pady=10)
    entry_id = tk.Entry(nova_janela)
    entry_id.insert(0, str(livro_id))
    entry_id.config(state="disabled")
    entry_id.pack(pady=10)

    tk.Label(nova_janela, text="Nome").pack(pady=10)
    entry_nome = tk.Entry(nova_janela)
    entry_nome.insert(0, str(lancamentos.get('nome', '')))
    entry_nome.pack(pady=10)

    tk.Label(nova_janela, text="Preço").pack(pady=10)
    entry_preco = tk.Entry(nova_janela)
    entry_preco.insert(0, str(lancamentos.get('preco', '')))
    entry_preco.pack(pady=10)
 
    tk.Label(nova_janela, text="ID Categoria").pack(pady=10)
    entry_idCategoria = tk.Entry(nova_janela)
    entry_idCategoria.insert(0, str(lancamentos.get('id_categoria', '')))
    entry_idCategoria.pack(pady=10)

    tk.Label(nova_janela, text="ID Autor").pack(pady=10)
    entry_idAutor = tk.Entry(nova_janela)
    entry_idAutor.insert(0, str(lancamentos.get('id_autor', '')))
    entry_idAutor.pack(pady=10)

    btn_salvar = tk.Button(nova_janela, text="Salvar", command=lambda:db.atualizar_livro(
        livro_id, entry_nome.get(), 
        entry_preco.get(), 
        entry_idCategoria.get(), 
        entry_idAutor.get(),
        nova_janela
        ))
    btn_salvar.pack(pady=10)
    
def tela_principal():

    root = tk.Tk()
    root.title("BIblioteca")
    root.geometry("600x600")

    btn_listagem_livros = tk.Button(root, text="Abrir Lista De Livros", command=janela_lista_livros)
    btn_listagem_livros.pack(pady=10)

    btn_janela_cadastra_livro = tk.Button(root, text="Cadastrar Livro", command=janela_cadastra_livro)
    btn_janela_cadastra_livro.pack(pady=10)

    root.mainloop()

