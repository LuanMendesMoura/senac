

def create_ong(nome,tipo,cnpj,):
    ong = {
        'nome':nome,
        'tipo':tipo,
        'CNPJ':cnpj,
        'projeto':[ ]

    }
    return ong

def create_projeto(nome,descricao):
    projeto = {
    'nome':nome,
    'descricao':descricao
    }
    return projeto

def localiza_ong(nome, catalogo):
    for ong in catalogo:
        if catalogo["nome"]==nome:
            return ong
    return None

def localiza_ong_index(nome,catalogo):
    for index in range(0,len(catalogo)):
        if catalogo[index]["nome"]==nome:
            return index
    return None