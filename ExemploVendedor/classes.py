class Vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas) :
           self.vendas = vendas

    def bateu_meta(self, meta):
         if self.vendas > meta:
            print(f"{self.nome} bateu a meta")
         else:
            print(f"{self.nome} não bateu a meta")
