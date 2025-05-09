# criando um exemplo de classe para Clientes da Netflix

class Cliente():
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.listaPlanos = ["Basic", "Premium"]
        if plano in self.listaPlanos:
            self.plano = plano
        else:
            raise Exception("Plano inválido")
        
    def mudarPlano(self, novoPlano):
        if novoPlano in self.listaPlanos:
            self.plano = novoPlano
            print(f"Plano alterado para {novoPlano}")
        else :
            raise Exception("Plano inválido")
    
    def verFilme(self, filme, planoFilme):
        if self.plano == planoFilme:
            print(f"Filme {filme} assistido com sucesso")
        else:
            raise Exception("Plano inválido para assistir esse filme")
        
# Exemplo de uso da classe Cliente
cliente = Cliente("João Pedro", "jpmarinw@gmail.com", "Basic")

print(cliente.plano)

cliente.verFilme("O senhor dos anéis", "Premium")