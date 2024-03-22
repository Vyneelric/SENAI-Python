a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
if a > b:
    aux = a
    a = b
    b = aux
if a > c:
    aux = a
    a = c
    c = aux
if b > c:
    aux = b
    b = c
    c = aux
print(f'{a} _ {b} _ {c}')