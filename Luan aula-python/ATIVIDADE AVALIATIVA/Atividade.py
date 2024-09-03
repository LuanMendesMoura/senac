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
        return f"Nome: {self.nome}\nDescrição: {self.descricao}\nResponsável: {self.responsavel}\nStatus: {self.status}"

class Ong:
    nome = ""
    projetos = []

    def __init__(self,nome):
        self.nome = nome

    def adicionar_projeto(self,projeto):
        self.projetos.append(projeto)

    def listar_projetos(self):
        print("Projetos: ")
        for projeto in self.projetos:
            print(projeto.nome)

    def buscar_projeto(self,nome):
        for projeto in self.projetos:
            if projeto.nome == nome:
                return projeto
        return None
    
projeto = Projeto("Educação Fisica","Atividades fisicas","Luan","Em andamento")
print(f"Nome: {projeto.nome}")

ong = Ong("Strong")
print(f"Nome da Ong: {ong.nome}")

ong.adicionar_projeto(projeto)

ong.listar_projetos()

projeto_valido = ong.buscar_projeto("Educação Fisica")
if projeto_valido != None:
    print(f"Projeto: {projeto_valido.nome}")
    print(f"Status: {projeto_valido.status}")
    projeto_valido.atualizar_status("Concluído ! ")
    print(f"Status atualizado: {projeto_valido.status}")
    print(f"Informações do projeto: {projeto_valido.mostrar_informacoes()}")
else:
    print("Projeto não encontrado ! ")

def menu_ong():
    nome = input("Informe o nome da Ong: ")

def menu_geral():
    print("1 - ")

def menu_projetos():
    nome = input("Informe o nome do Projeto: ")
    descricao = input("Informe o objetivo do Projeto: ")
    responsavel = input("Informe o nome do responsável pelo Projeto: ")
    status = input("Informe o status do Projeto: ")
    projeto = Projeto(nome,descricao,responsavel,status)
while True:
    menu_ong()