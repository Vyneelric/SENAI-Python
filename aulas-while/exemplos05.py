total = 0
resposta = input('deseja iniciar a compra? [s/n]: ')
while resposta == 's':
    valor = int(input('digite o valor do item: '))
    total = total + valor
    resposta = input('Deseja adicionar mais um produto? [s/n]: ')
print (f'Total da compra: {total}')