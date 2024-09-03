import http.client
import json
from time import sleep
# http_request = http.client.HTTPSConnection("brasilapi.com.br")
# http_request.request("GET","/api/cep/v1/79014050")
# response = http_request.getresponse()
# resposta_bytes = response.read()
# json_ = json.loads(resposta_bytes)

# for key in json_.keys():
#     print(f"{key} : {json_[key]}")

# cep = input("INSIRA SEU CEP: ")

# http_request = http.client.HTTPSConnection("brasilapi.com.br")
# http_request.request("GET",f"/api/cep/v1/{cep}")
# response = http_request.getresponse()
# resposta_bytes = response.read()
# json_ = json.loads(resposta_bytes)

# for key in json_.keys():
#     print(f"{key} : {json_[key]}")

def api(url):
    http_request = http.client.HTTPSConnection("brasilapi.com.br")
    http_request.request("GET",f"{url}")
    response = http_request.getresponse()
    resposta_bytes = response.read()
    json_ = json.loads(resposta_bytes)
    return json_

def print_json_key(object):
    if type(object) is list:
        for json_ in object:
            for key in json_.keys():
                print(f"{key} : {json_[key]}")

    elif type(object) is dict:
        for key in object.keys():
            print(f"{key} : {object[key]}")


def espaco(nome):
    return str(nome).replace(" ","%20")

def menu():
    print("1 - CEP\n2 - CNPJ\n3 - DDD\n4 - FERIADOS NACIONAIS\n5 - MUNICIPIOS DO UF\n6 - BUSCAR CIDADES\n7 - BUSCAR BANCO\n8 - PREÇO TABELA FIPE\n9 - SAIR")

sair = True
while sair:
    menu()
    op = int(input("INSIRA UMA OPÇÃO: "))
    if op == 1:
        cep = input("INSIRA O CEP: ")
        json_cep = api(f"/api/cep/v1/{cep}")
        print_json_key(json_cep)
    elif op == 2:
        cnpj = input("INSIRA O CNPJ: ")
        json_cnpj = api(f"/api/cnpj/v1/{cnpj}")
        print_json_key(json_cnpj)
    elif op == 3:
        ddd = input("INSIRA O DDD: ")
        json_ddd = api(f"/api/ddd/v1/{ddd}")
        print_json_key(json_ddd)
    elif op == 4:
        ano = input("INSIRA O ANO: ")
        json_ano = api(f"/api/feriados/v1/{ano}")
        print_json_key(json_ano)
    elif op == 5:
        municipios = input("INSIRA SIGLA DA UF: ")
        json_municipio = api(f"/api/ibge/municipios/v1/{municipios}?providers=dados-abertos-br,gov,wikipedia")
        print_json_key(json_municipio)
    elif op == 6:
        cidade = espaco(input("INSIRA O NOME DA CIDADE: "))
        json_cidade = api(f"/api/cptec/v1/cidade/{cidade}")
        print_json_key(json_cidade)
    elif op == 7:
        banco = input("INSIRA O CÓDIGO DO BANCO: ")
        json_banco = api(f"/api/banks/v1/{banco}")
        print_json_key(json_banco)
    elif op == 8:
        fipe = input("INSIRA O CÓDIGO FIPE: ")
        json_fipe = api(f"/api/fipe/preco/v1/{fipe}")
        print_json_key(json_fipe)
    # elif op == 9:
    #     codigo = input("INSIRA O CÓDIGO DA CIDADE: ") 
    #     dias = input("DIAS DESEJADOS PARA PREVISÃO: ")   
    #     json_clima = api(f"/api/cptec/v1/clima/previsao/{codigo}/{dias}")
    #     print_json_key(json_clima)
    elif op == 9:
        for i in range(5,0,-1):
            print(f"SAINDO EM: {i}")
            sleep(1)
        sair = False
        