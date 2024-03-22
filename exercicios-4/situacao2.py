media = float(input('Digite sua média: '))

if media >= 7:
    print ('Aprovado!!!')
else:
    print('vc é muito burro kkk')
    nota_recuperacao = float(input('Digite a nota de recuperação: '))
    media_recuperacao = (media + nota_recuperacao) / 2
    if media_recuperacao >= 7:
        print ('Aprovado!!!')
    else:
        print ('vc é um animal, foi reprovado')
print (media_recuperacao)

