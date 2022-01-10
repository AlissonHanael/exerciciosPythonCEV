r1 = float(input('Digite o valor para lado 1: '))
r2 = float(input('Digite o valor para lado 2: '))
r3 = float(input('Digite o valor para lado 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Pode formar triangulo')
else:
    print('NÃO Pode formar triangulo')
