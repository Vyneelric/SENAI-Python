nome = input('digite teu nome rapá: ')
media = float(input('digite sua média: '))
freq =  int(input('digite sua frequência: '))

#f'-> uma string (cometario) que lê variaveis com as chaves {}
if media >= 7 and freq >= 75:
    print(f'{nome} Você foi aprovado e sua média é: {media}, sua frequência é: {freq}')
else: 
    print('Reprovado')
