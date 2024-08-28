a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
c = int(input("Digite um valor para C: "))
delta = b ** 2 - 4

if delta < 0:
    print ("Não há solução real!")
elif delta == 0: 
    x = (-b + delta ** (1/2)) / 2 * a
    print (f'x = {x}')
else:
    x1 = (-b + delta ** (1/2)) / 2 * a
    x2 = (-b - delta ** (1/2)) / 2 * a
    print (f"x1 = {x1}")
    print (f"x2 = {x2}")