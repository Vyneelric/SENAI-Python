import os
from matematica import *
from colorama import init, Fore

init(autoreset = True)

def limpar_tela():
    os.system("clear")
    
def pause():
    input(f"{Fore.GREEN}Digite ENTER para continuar...{Fore.RESET}")

def exibir_menu():
    print ("1 - Verificar se o número é PAR/IMPAR")
    print ("2 - Somatório")
    print ("3 - Fatorial")
    print ("0 - Sair")  

def escolher_opcao(opcao):
    if opcao == "1":
        numero = int(input("Digite um número: "))
        resposta = par_impar(numero)
        print(resposta)
    elif opcao == "2":
        numero = int(input("Digite um número: "))
        resposta = calcular_somatorio(numero)
        print (resposta)
    elif opcao == "3":
        numero = int(input("Digite um número: "))
        resposta = calcular_fatorial(numero)
        print (resposta)
    elif opcao == "0":
        print ("Fechando o Sistema...")
    else:
        print (f"{Fore.RED}Opcão Inválida, Tente: (0 - 1 - 2 - 3){Fore.RESET}")


def iniciar_sys():
    limpar_tela()
    exibir_menu()
    opcao_escolhida = input('Escolha uma opção: ')
    escolher_opcao (opcao_escolhida)
    pause()
    iniciar_sys()

iniciar_sys()