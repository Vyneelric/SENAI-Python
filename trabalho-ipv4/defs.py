from colorama import init, Fore
ip = input('digite seu ip: ')
separado = ip.split('.')
separado1 = [int(separado[0]), int(separado[1]), int(separado[2]), int(separado[3])]

def classe():
    if separado1[0] >0 and separado1[0]<=127:
        print(f'{Fore.YELLOW}o ip esta na classe a{Fore.RESET}')
    elif separado1[0] >=128 and separado1[0]<=191:
        print(f'{Fore.BLUE}o ip esta na classe b{Fore.RESET}')
    elif separado1[0] >=192 and separado1[0] <=223:
        print(f'{Fore.GREEN}o ip esta na classe c{Fore.RESET}')
def mascara():
    if separado1[0] >0 and separado1[0]<=127:
        print(f'{Fore.LIGHTBLACK_EX}a mascara de subrede é 255.0.0.0{Fore.RESET}')
    if separado1[0] >=128 and separado1[0]<=191:
        print(f'{Fore.LIGHTMAGENTA_EX}a mascara de subrede é 255.255.0.0{Fore.RESET}')
    if separado1[0] >=192 and separado1[0] <=223:
        print(f'{Fore.CYAN}a mascara de subrede é 255.255.255.0{Fore.RESET}')
def comeco_rede():
    if separado1[0] >0 and separado1[0]<=127:
        separado1[3] = 0
        separado1[2] = 0
        separado1[1] = 0
        print(f'{Fore.LIGHTYELLOW_EX}o começo da rede é:  {separado1[0]}.{separado1[1]}.{separado1[2]}.{separado1[3]} {Fore.RESET}')
    if separado1[0] >=128 and separado1[0]<=191:
        separado1[2] = 0
        separado1[3] = 0
        print(f'{Fore.RED}o começo da rede é:  {separado1[0]}.{separado1[1]}.{separado1[2]}.{separado1[3]} {Fore.RESET}')
    elif separado1[0] >=192 and separado1[0] <=223:
        separado1[3] = 0
        print(f'o começo da rede é:  {separado1[0]}.{separado1[1]}.{separado1[2]}.{separado1[3]}')
def primeiro_ip():
    if separado1[0] >0 and separado1[0]<=127:
        separado1[3] = 1
        print(f'o primeiro IP valido é:  {separado1[0]}.{separado1[1]}.{separado1[2]}.{separado1[3]}')
    if separado1[0] >=128 and separado1[0]<=191:
        separado1[2] = 0
        separado1[3] = 1
        print(f'o primeiro IP valido é:  {separado1[0]}.{separado1[1]}.{separado1[2]}.{separado1[3]}')
    elif separado1[0] >=192 and separado1[0] <=223:
        separado1[1] = 0
        separado1[2] = 0
        separado1[3] = 1
        print(f'o primeiro IP valido é:  {separado1[0]}.{separado1[1]}.{separado1[2]}.{separado1[3]}')
def ultimo_ip():
    if separado1[0] >0 and separado1[0]<=127:
        separado1[1] = 255
        separado1[2] = 255
        separado1[3] = 254
        print(f'o ultimo IP valido é:  {separado1[0]}.{separado1[1]}.{separado1[2]}.{separado1[3]}')
    if separado1[0] >=128 and separado1[0]<=191:
        separado1[2] = 255
        separado1[3] = 254
        print(f'o ultimo IP valido é:  {separado1[0]}.{separado1[1]}.{separado1[2]}.{separado1[3]}')
    if separado1[0] >=192 and separado1[0] <=223:
        separado1[3] = 254
        print(f'o ultimo IP valido é:  {separado1[0]}.{separado1[1]}.{separado1[2]}.{separado1[3]}')
def broadcast():
    if separado1[0] >0 and separado1[0]<=127:
        separado1[3] = 255
        separado1[2] = 255
        separado1[1] = 255
        print(f'o broadcast é:  {separado1[0]}.{separado1[1]}.{separado1[2]}.{separado1[3]}')
    if separado1[0] >=128 and separado1[0]<=191:
        separado1[2] = 255
        separado1[3] = 255
        print(f'o broadcast é:  {separado1[0]}.{separado1[1]}.{separado1[2]}.{separado1[3]}')
    if separado1[0] >=192 and separado1[0] <=223:
        separado1[3] = 255
        print(f'o broadcast é:  {separado1[0]}.{separado1[1]}.{separado1[2]}.{separado1[3]}')