from api_client import *
import getpass


def create_login():
    nome=input("Login: ")
    senha=getpass.getpass("Senha: ")
    senha_confirma=getpass.getpass("Confirma Senha: ")
    if senha==senha_confirma:    
        json_= {'nome':nome,'senha':senha}
        response = api_create_login(json_)
        if response.status_code ==200 or response.status_code==201:
            return True
    return False

def login():
    nome=input("Login: ")
    senha=getpass.getpass("Senha: ")
    json_= {'nome':nome,'senha':senha}
    response = api_login(json_)
    if response.status_code ==200 or response.status_code==201:
        return json.loads(response.content)['token']
    return None

