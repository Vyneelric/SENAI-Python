Nome = str (input('digite o seu nome: '))
Dependentes = int (input('digite o número de dependentes: '))
HorasTrabalhadas = int (input('digite o número de horas trabalhadas: '))
ValorHora = 20
salarioBruto = (HorasTrabalhadas * ValorHora)
HoraFamilia = int

if salarioBruto > 4000:
    HoraFamilia = 5
if salarioBruto < 1000:
    HoraFamilia = 10
if salarioBruto <= 1000 and 4000:
    HoraFamilia = 7,50

salarioFamilia = (HorasTrabalhadas * HoraFamilia)
salarioFinal = (salarioBruto + salarioFamilia)

print('/////////////////////////////////////////////')
print(f'Seu nome: {Nome}')
print(f' Quantidade de dependes: {Dependentes}')
print(f' Quantidade de Horas trabalhadas: {HorasTrabalhadas}')
print(f' Valor hora de trabalho: {ValorHora}')
print(f' Valor hora familia: {HoraFamilia}')
print(f' Valor do Salario Bruto: {salarioBruto}')
print(f' Valor do Salario Família: {salarioFamilia}')
print(f' Salario Final: {salarioFinal}')
print('/////////////////////////////////////////////')