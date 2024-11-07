import tkinter as tk
import database as db

def tela_principal():
    root = tk.Tk()
    root.title("BIblioteca")
    root.geometry("600x600")

    tk.Button(root, text="IMPRIMIR PRODUTOS", width=30, command=lambda: db.buscar_todos('livros')).pack(pady=10)

    tk.Label(root, text="NOME DO LIVRO", width=50).pack()
    
    input_livro = tk.Entry(root)
    input_livro.pack()

    tk.Button(root, text="BUSCAR", width=30, command=lambda: db.buscar_livro_nome(input_livro.get())).pack(pady=10)

    root.mainloop()