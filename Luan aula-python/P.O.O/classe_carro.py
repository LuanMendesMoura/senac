class Base():
    marca=''
    modelo=''
    ano=''
    cor=''
    status_motor=False
    def __init__(self,marca=None,cor=None,modelo=None,ano=None):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Carro(Base):
    velocidade =0
    combustivel =20

    def ligar_motor(self):
        print("Motor ligado !")
        self.status_motor = True

    def desligar_motor(self):
        print("Motor desligado !")
        self.status_motor = False

    def status_motor_painel(self):
        print(self.status_motor)
        print(f"Velocidade: {self.velocidade}")
        print(f"Combustível: {self.combustivel}litros")
        if self.combustivel <= 5:
            print("CARRO NA RESERVA ! ")

    def acelerar(self):
        if self.status_motor == True:
            print("Acelerando !")
            for i in range(0,10):
                self.velocidade +=1
                self.combustivel -=0.1
                n = round(self.combustivel,2)
                self.combustivel = n
                print(n) 
        else:
            print("Carro desligado !")

    def frear(self):
        print("Freando !")
        for i in range(0,10):
            self.velocidade += -1

    def abastecer(self):
        for i in():
            self.combustivel = self.combustivel + 0.10
        print()
        print("Abastecendo !")
        