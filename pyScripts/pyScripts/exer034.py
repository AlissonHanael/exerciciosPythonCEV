salario = float(input('Digite o seu salario: '))
if salario <= 1250 and salario > 0:
    novoSalario = salario + (salario*0.15)
    print('Valor total do seu novo salario: R${:.2f}'.format(novoSalario))
else:
    novoSalario = salario + (salario*0.1)
    print('Valor total do seu novo salario: R${:.2f}'.format(novoSalario))
