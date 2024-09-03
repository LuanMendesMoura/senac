from classes import ONG,Projeto
from api_client import *



def createOng(token):
    nome_ong = ONG(input("Nome ONG: "))
    ong = ONG(nome_ong)
    nome_projeto = input("Nome Projeto: ")
    descricao_projeto = input("Descrição Projeto: ")
    resposavel_projeto = input("Responsável Projeto: ")
    status_projeto = input("Status Projeto: ")
    projeto = Projeto(nome_projeto,descricao_projeto,resposavel_projeto,status_projeto)
    ong.adicionar_projeto(projeto)
    print(api_create(ong.to_json(),token))


def getOngs():  
    ongs=[]  
    ongs_json=api_read()
    for index, data in zip(range(len(ongs_json)),ongs_json):
        ong = ONG(nome=data['nome'],_id=data['_id'])
        print(f'{index} : Nome: {data['nome']}')
        for p in data['projetos']:
            projeto = Projeto(p['nome'],p['descricao'],
                              p['responsavel'],p['status'],p['_id'])
            ong.adicionar_projeto(projeto)
            print(f'  Projeto ----> {p['nome']}')
        ongs.append(ong)
        print('\n')
    return ongs