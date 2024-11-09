import mysql.connector
import tkinter as tk

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
