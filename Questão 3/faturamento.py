import json

with open("dados.json") as dadosFaturamento:
    dados = json.load(dadosFaturamento)

menor = 0
maior = 0
contDias = 0
valorTotal = 0
contDiasFatSuperior = 0

for d in dados:
    if(menor > d['valor']):
        menor = d['valor']
    if(maior < d['valor']):
        maior = d['valor']
    if d['valor'] != 0:
        contDias+=1
        valorTotal += d['valor']

mediaMensal = valorTotal / contDias

for d in dados:
    if(d['valor'] > mediaMensal):
        contDiasFatSuperior += 1

print(f'O menor valor de faturamento foi: {menor:.2f}\nO maior valor de faturamento foi: {maior:.2f}')
print(f'O faturamento diário foi maior do que a média mensal durante {contDiasFatSuperior} dias')

