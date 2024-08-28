a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


def fato(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado


for numero in a:
    resultado = fato(numero)
    print(f'O fatorial de: {numero} é {resultado}')


