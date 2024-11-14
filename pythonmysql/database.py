import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
import ui

# class Livro():
#     nome:str
#     preco:float
#     id_categoria:int
#     id_autor:int

def conexao_banco():
    try:
        cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='biblioteca'
        )

        return cnx
        # print("Deu certo a conexão")
    except:
        print("Deu erro na conexão")

def buscar_todos(tabela):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()
        query = 'SELECT id, nome, preco FROM {}'.format(tabela)
        cursor.execute(query)
        registros = cursor.fetchall()

        # print(registros)

        # nomes = "\n".join(registro[0] for registro in registros)

        return registros

    except:
        print("Não foi possível selecionar todos da tabela {}".format(tabela))
    
    finally:
        cursor.close()

def buscar_livro_nome(nome, tree):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()
        query = "SELECT * FROM livros WHERE nome LIKE '%{}%'".format(nome)
        cursor.execute(query)
        registros = cursor.fetchall()

        for registro in registros:
            tree.insert("", tk.END, values=registro)

        return registro
    
    except:
        print("Não encontrei esse registro")

    finally:
        cursor.close()

def cadastrar_livro(nome,preco,id_categoria,id_autor):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()

        query = "INSERT INTO livros (nome, preco, id_categoria, id_autor) VALUES (%s, %s, %s, %s)"

        cursor.execute(query,(nome,preco,id_categoria,id_autor))

        conexao.commit()

        messagebox.showinfo("SUCESSO", "Livro cadastrado com sucesso!")

    except:
        messagebox.showerror("ERRO", "Não foi possível inserir o livro")
    
    finally:
        cursor.close()

def delete_livro(livro_id):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()

        query = "DELETE FROM livros WHERE id = {}".format(livro_id)

        cursor.execute(query)

        conexao.commit()

        messagebox.showinfo("SUCESSO", "Livro deletado com sucesso!")

    except:
        messagebox.showerror("ERRO", "Não foi possível deletar o livro")

    finally:
        cursor.close()

def atualizar_livro(livro_id,nome,preco,id_categoria,id_autor):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()

        query = """UPDATE livros 
        SET nome = %s, preco = %s, id_categoria = %s, id_autor = %s
        WHERE id = %s"""

        cursor.execute(query, (nome,preco,id_categoria,id_autor,livro_id))

        conexao.commit()

        messagebox.showinfo("SUCESSO", "Livro atualizado com sucesso!")

    except:
        messagebox.showerror("ERRO", "Não foi possível atualizar o livro")

    finally:
        cursor.close()
        