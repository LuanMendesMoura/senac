import classe_carro

carros = []
while True:
    print("1 - CRIAR CARRO\n2 - SELECIONAR CARRO")
    op = int(input("INSIRA UMA OPÇÃO: "))
    if op == 1:
        _cor = input("INFORME A COR: ")
        _marca = input("INFORME A MARCA: ")
        _modelo = input("INFORME O MODELO: ")
        _ano = input("INFORME O ANO: ")
        carro = classe_carro.Carro(_marca,_cor,_modelo,_ano)
        carros.append(carro)
    
    elif op == 2:
        op = int(input("SELECIONE O CARRO: "))
        carro_selecionado = carros[op]
        op = int(input("""1 - LIGAR MOTOR\n2 - DESLIGAR MOTOR\n3 - ACELERAR\n4 - FREAR\n5 - PAINEL
6 - REMOVER CARRO\nINSIRA UMA OPÇÃO: """))
        if op == 1:
            carro_selecionado.ligar_motor()
        elif op == 2:
            carro_selecionado.desligar_motor()
        elif op == 3:
            carro_selecionado.acelerar()
        elif op == 4:
            carro_selecionado.frear()
        elif op == 5:
            carro_selecionado.status_motor_painel()
        elif op == 6:
            carros.pop(carro)
