from utilitarios import (cadastrar_categoria, cadastrar_transacao, saldo_total)

cat_receita =cadastrar_categoria("Receitas")
cat_despesas = cadastrar_categoria("Despesas")
cat_viagens =cadastrar_categoria("Viagens")

salario = cadastrar_transacao("Salário", 5000, cat_receita)
aluguel = cadastrar_transacao("Aluguel", 1000, cat_despesas)
luz = cadastrar_transacao("Conta de Luz", 99.90, cat_despesas)
viagem = cadastrar_transacao("Viagem para SP", 300, cat_despesas)

print(f"O saldo total de seu salário de R${salario.valor}, após pagar aluguel de R${aluguel.valor} e conta de luz de R${luz.valor} e a viagem de R${viagem.valor} é de R${saldo_total()}")