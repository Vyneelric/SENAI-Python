#array; tamanho (quantidade de números) e índice (começa do 0)
#para achar o índice (qnt - 1)

nomes = ['Ana','Victoria', 'Bomba', 'dog', ]
numeros = [47, 93, 52, 72, 18]

contador = 0
ult_idc = len(nomes) - 1
while contador <= ult_idc:
    print(nomes[contador])
    contador = contador + 1

contador = 0
ult_idc = len(numeros) - 1
while contador <= ult_idc:
    valor_desconto = numeros[contador] - 5
    print(valor_desconto)
    contador = contador + 1
