#: - faça
#!= - diferente
#def - tipo uma pasta
#== - tipo uma pergunta
#função para mostrar o MENU
def mostrar_opcoes():
    print('Escolha uma opção: ')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Somátoria')
    print('6 - Fatorial')
    print('0 - Sair')

#função para pegar os valores para o resultado
def pegar_valores():
    n1 = int(input('primeiro valor: '))
    n2 = int(input('segundo valor: '))
    return n1, n2

#função para fazer a soma dos valores
def soma(a, b):
    return a + b 

def subtracao(a, b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a/b

def somatorio(numero):
    contador = 1
    s = 0
    while contador <= numero:
        s = s + contador 
        contador = contador + 1
    return s
    
def fato(numero):
    contador = 1
    f = 1
    while contador <= numero:
        f = f * contador 
        contador = contador + 1
    return f


#repetição para funcionar o código e fazer a repetição
resposta = 1
while resposta != '0':
    mostrar_opcoes()
    resposta = input('-> ')
    if resposta == '1':
        n1, n2 = pegar_valores()
        resultado = soma(n1, n2)
        print(f'A soma dos número é: {resultado}')
    elif resposta == '2':
        n1, n2 = pegar_valores()
        resultado = subtracao(n1,n2)
        print(f'A diferença dos valores é: {resultado}')
    elif resposta == '3':
        n1, n2 = pegar_valores()
        resultado = mult(n1,n2)
        print(f'O resultado da multiplicação é de: {resultado}')
    elif resposta == '4':
        n1, n2 = pegar_valores()
        resultado = div(n1,n2)
        print(f'A divisão entre os números foi de: {resultado}')
    elif resposta == '5':
        n1, n2 = pegar_valores()
        resultado1 = somatorio(n1)
        resultado2 = somatorio(n2)
        print(f'A somatória de {n1} é: {resultado1}')
        print(f'A somatória de {n2} é: {resultado2}')
    elif resposta == '6':
        n1, n2 = pegar_valores()
        resultado3 = fato(n1)
        resultado4 = fato(n2)
        print(f'O fatorial de {n1} é: {resultado3}')
        print(f'O fatorial de {n2} é: {resultado4}')
    elif resposta == '0':
        print ('saindo do system...')
    else:
        print ('Opção inválida, tente novamente')