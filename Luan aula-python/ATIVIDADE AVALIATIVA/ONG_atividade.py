import http.client
import json

class Projeto:  
    nome = ""  
    descricao = ""  
    responsavel = ""  
    status = ""  

    def __init__(self,nome=None,descricao=None,responsavel=None,status=None):  
        self.nome = nome  
        self.descricao = descricao  
        self.responsavel = responsavel   
        self.status = status  
 
    def atualizar_status(self,novo_status=None):  
        self.status = novo_status  

    def mostrar_informacoes(self):  
        return f"\nNOME: {self.nome}\nDESCRIÇÃO: {self.descricao}\nRESPONSÁVEL: {self.responsavel}\nSTATUS: {self.status}"  


class Ong:  
    nome = ""  
    projetos = []  

    def __init__(self,nome=None):  
        self.nome = nome  

    def adicionar_projeto(self,projeto):  
        self.projetos.append(projeto)  

    def listar_projetos(self):  
        print("\nPROJETOS: ")  
        for projeto in self.projetos:  
            print(projeto.nome)  
 
    def buscar_projeto(self,nome):  
        for projeto in self.projetos:  
            if projeto.nome == nome:  
                return projeto  
        return None
      
def view_menu():  
    print("""\n1 - CRIAR UMA ONG\n2 - ADICIONAR PROJETO\n3 - LISTAR PROJETOS\n4 - BUSCAR PROJETOS\n5 - FECHAR""") 

class Gerenciador_Ong():    
    ongs = []
    
    def __init__(self):
        json_ongs = self.api("/v3/b/66985766acd3cb34a8679cdf")['record']
        for ongs in json_ongs['ongs']:
            ong = Ong(ongs['nome'])
            print(f'Nome Ong : {ongs['nome']}')
            for projeto in ongs['projetos']:
                print(f'---->Projeto : {projeto['nome']}')
                projeto = Projeto(projeto['nome'],projeto['descricao'],projeto['responsavel'],projeto['status'])
                ong.adicionar_projeto(projeto)
            self.adicionar_ong(ong)

    def api(self,url):
        http_request = http.client.HTTPSConnection('api.jsonbin.io')
        http_request.request("GET",url)
        response = http_request.getresponse()
        resposta_bytes = response.read()
        json_ = json.loads(resposta_bytes)
        return json_
    
    def adicionar_ong(self,ong):
        self.ongs.append(ong)

    def listar_ong(self):
        for ong in self.ongs:
            print(ong.nome)

gerenciador = Gerenciador_Ong()
# ongs = gerenciador.ongs


# sair = True 
# while sair: 
#     view_menu() 
#     op = int(input("INSIRA UMA OPÇÃO: ")) 
#     if op == 1: 
#         nome_ong = input("INFORME O NOME DA ONG: ")  
#         ong = Ong(nome_ong)
#     elif op == 2: 
#         if type(ong) is not Ong: 
#             print("PRECISA CRIAR UMA ONG ! ") 
#         else: 
#             nome_projeto = input("INFORME O NOME DO PROJETO: ")  
#             descricao = input("INFORME O OBJETIVO DO PROJETO: ")  
#             responsavel = input("INFORME O NOME DO RESPONSÁVEL PELO PROJETO: ")  
#             status = input("INFORME O STATUS DO PROJETO: ")  
#             projeto = Projeto(nome_projeto,descricao,responsavel,status) 
#             ong.adicionar_projeto(projeto) 
#     elif op == 3: 
#         ong.listar_projetos() 
#     elif op == 4: 
#         nome = input("INSIRA O NOME DO PROJETO: ")  
#         projeto_valido = ong.buscar_projeto(nome) 
#         if projeto_valido != None: 
#             print(f"PROJETO: {projeto_valido.nome}")  
#             print(f"STATUS: {projeto_valido.status}")  
#             print(f"\nINFORMAÇÕES DO PROJETO: {projeto_valido.mostrar_informacoes()}")  
#             print("\n1 - ATUALIZAR STATUS\n2 - VOLTAR") 
#             op = int(input("INSIRA UMA OPÇÃO: ")) 
#             if op == 1: 
#                 status = input("INFORME O STATUS DO PROJETO: ")  
#                 projeto_valido.atualizar_status(status) 
#                 print(f"STATUS ATUALIZADO: {projeto_valido.status}")  
#             elif op == 2: 
#                 pass 
#         else: 
#             print("\nPROJETO NÃO ENCONTRADO !\nINSIRA 4 PARA VER SEUS PROJETOS ! ") 
#     elif op == 5: 
#         from time import sleep 
#         for i in range(5,0,-1): 
#             print(f"FECHANDO EM: {i}") 
#             sleep(1) 
#         sair = False
