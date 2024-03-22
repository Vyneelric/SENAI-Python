atual = 1
anterior = 0
proximo = 1
while proximo <= 987:
    print(anterior)
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    proximo = proximo + 1