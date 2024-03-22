def mostrar_opcoes():
    print('Escolha uma opção: ')
    print('1 - Triângulo')
    print('2 - Quadriátero')
    print('3 - Círculo')
    print('0 - Sair')

def pegar_valores_q():
    n1 = int(input('primeira reta: '))
    n2 = int(input('segunda reta: '))
    n3 = int(input('terceira reta: '))
    n4 = int(input('quarta reta: '))
    return n1, n2, n3, n4

def quadrado(a,b,c,d):
    a = b , c = d 
    return a,b,c,d 

resposta = 1
while resposta != '0':
    mostrar_opcoes()
    resposta = input('-> ')
    if resposta == '2':
        n1 = pegar_valores_q()
        resultado = quadrado()
        print(f'Ele é um quadrado: {resultado}')
    else:
        print('Ele num é um quadrado')