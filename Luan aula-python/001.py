import json
import http.client

class Projeto:  
    _id = str
    nome = str  
    descricao = str  
    responsavel = str
    status = str 

    def __init__(self,nome=None,descricao=None,responsavel=None,status=None,_id=None):  
        self.nome = nome  
        self.descricao = descricao  
        self.responsavel = responsavel   
        self.status = status  
        self._id = _id
 
    def atualizar_status(self,novo_status=None):  
        self.status = novo_status  

    def mostrar_informacoes(self):  
        return f"\nNOME: {self.nome}\nDESCRIÇÃO: {self.descricao}\nRESPONSÁVEL: {self.responsavel}\nSTATUS: {self.status}"  
    
    def to_json(self):
        json_ = { }
        json_['nome'] = self.nome
        json_['descricao'] = self.descricao
        json_['responsavel'] = self.responsavel
        json_['status'] = self.status
        return json_
    

class Ong:  
    _id = str
    nome = str  
    projetos = []  

    def __init__(self,nome=None,_id=None):  
        self.nome = nome
        self._id = _id  

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
    
    def to_json(self):
        json_ = { }
        json_['nome'] = self.nome
        json_['projetos'] = []  
        for projeto in self.projetos:
            p = projeto.to_json()
            json_['projetos'].append(p)
        return json_



class Gerenciador_Ong: 
    ongs = []   

    def __init__(self):
        pass

    def carregar_dados(self):
        self.ongs = []
        json_ongs = self.api_get()
        for ongs in json_ongs:
            ong = Ong(ongs['nome'])
            print(f"Nome Ong : {ongs['nome']}")
            for projeto in ongs['projetos']:
                projeto = Projeto(projeto['nome'],projeto['descricao'],projeto['responsavel'],projeto['status'])
                ong.adicionar_projeto(projeto)
            self.adicionar_ong(ong)

    def api_get(self):
        http_request = http.client.HTTPSConnection('api.viana.dev')
        headers = {'Content-type': 'application/json'}
        http_request.request("GET",'/ongs', headers=headers)
        response = http_request.getresponse()
        resposta_bytes = response.read()
        json_ = json.loads(resposta_bytes)
        return json_
    
    def adicionar_ong(self,ong):
        self.ongs.append(ong)

    def api_create(self,ong_json):
        http_request = http.client.HTTPSConnection('api.viana.dev')
        headers = {'Content-type': 'application/json'}
        http_request.request("POST",'/ongs',body=ong_json,headers=headers)
        response = http_request.getresponse()
        resposta_bytes = response.read()
        json_ = json.loads(resposta_bytes)
        return json_

def view_menu():  
    print("""\n1 - CRIAR UMA ONG\n2 - ADICIONAR PROJETO\n3 - LISTAR PROJETOS\n4 - BUSCAR PROJETOS\n5 - FECHAR""") 

gerenciador = Gerenciador_Ong()

ong = Ong("LUAN MENDES MOURA")
projeto = Projeto("GRANDES ANIMAIS","CUIDA DE ANIMAIS ABANDONADOS !","LUAN","EM ANDAMENTO")
ong.adicionar_projeto(projeto)
projeto = Projeto("ADOTE ME","LOCAL DE ADOÇÂO DE ANIMAIS !","LUAN","EM ANDAMENTO")
ong.adicionar_projeto(projeto)

json_ = json.dumps(ong.to_json())
print(json_)
gerenciador.api_create(json_)


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
