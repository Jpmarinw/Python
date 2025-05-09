class Jogador:
    def __init__(self, altura, velocidade, passe, drible, precisao):
        self.altura = altura
        self.velocidade = velocidade
        self.passe = passe
        self.drible = drible
        self.precisao = precisao

    def passar(self):
        print("Mirar")
        print("Encostar na bola com a força de passe do jogador")
    
    def chutar(self):
        print("Mirar")
        print("Encostar na bola com a força de chute do jogador")
    
class Jogador_Goleiro(Jogador):
    def agarrar(self):
        print("Pular")
        print("Se estica para pegar a bola")
    
    def defender(self):
        esta_na_area = True
        if esta_na_area:
            print("Pode usar o corpo todo para defender")
            print("Defendeu")
        else:
            print("Pode usar apenas pernas, tronco e ombros para defender")
            print("Defendeu")
              
class Jogador_Linha(Jogador):
    def defender(self):
        print("Pode usar apenas pernas, tronco e ombros para defender")
        print("Defendeu")

jogador1 = Jogador_Goleiro(1.90, 60, 70, 40, 70)
jogador2 = Jogador_Linha(1.75, 85, 80, 90, 80)

jogador1.defender()
jogador2.defender()