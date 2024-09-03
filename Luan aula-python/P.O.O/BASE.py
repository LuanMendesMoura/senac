class Banco():
    pe = ''
    assento = ''
    def __init__(self,assento=None,pe=None):
        self.assento = assento
        self.pe = pe
banco = Banco('acolchoado','rodas')

class Cadeira(Banco):
    encosto = ''
    braco = ''
    def __init__(self,encosto=None,braco=None,assento=None,pe=None):
        self.encosto = encosto
        self.braco = braco
        super().__init__(assento,pe)
cadeira = Cadeira('fixo','ajustavel')

print(cadeira)