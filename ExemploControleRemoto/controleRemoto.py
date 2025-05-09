class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
    
    def passarCanal(self, botao):
        if botao == "+":
            print("Canal aumentado")
        elif botao == "-":
            print("Canal diminuido")
        else:
            print("Canal inexistente")

    def aumentarVolume(self, volume):
        if volume < 100:
            volume += 1
            print(f"Volume aumentado para {volume}")
        else:
            print("Volume máximo atingido")
            
controleRemoto = ControleRemoto("preto", "10cm", "5cm", "3cm")
print(f"Controle remoto de cor {controleRemoto.cor}, altura {controleRemoto.altura}, profundidade {controleRemoto.profundidade} e largura {controleRemoto.largura}")

controleRemoto.aumentarVolume(50)
controleRemoto.passarCanal("+")