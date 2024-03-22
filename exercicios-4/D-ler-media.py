n1 = int(input('digite a nota1: '))
n2 = int(input('digite a nota2: '))
n3 = int(input('digite a nota3: '))
n4 = int(input('digite a nota4: '))

md1 = (n1 + n2 + n3 + n4) /4
if  md1 >= 7 :
    print('aprovado')
else:
   ne = int(input('digite a nota5: '))
md2 = (ne + md1) /4

if md2 >= 5 :
    print(f'{md2} aprovado')
else:
    print(f'{md2} reprovado')
