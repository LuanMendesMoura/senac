from classes import *



def view_projetos(projetos:list[Projeto]):
    for index,p in zip(range(len(projetos)),projetos):
        print(f'[{index}]: {p.nome}')
    

def view_ongs(ongs:list[ONG]):    
    for index, ong in zip(range(len(ongs)),ongs):
        print(f'{index} : Nome: {ong.nome}')
        for p in ong.getProjetos():
            print(f'  Projeto ----> {p.nome}')
        print('\n')
    
    