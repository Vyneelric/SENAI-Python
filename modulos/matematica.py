import os
def par_impar(numero):
    if numero % 2 == 0:
        return ("PAR")
    else:
        return("IMPAR")

def calcular_somatorio(numero):
    contador = 1
    soma = 0
    while contador <= numero:
        soma = soma + contador
        contador = contador + 1
    return soma

def calcular_fatorial(numero):
    contador = 1
    fatorial = 1
    while contador <= numero:
        fatorial = fatorial * contador
        contador = contador + 1
    return fatorial