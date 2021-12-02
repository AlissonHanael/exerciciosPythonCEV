import math as m
num = float(input('Digite um número real: '))
print('O valor arredondado para o próximo maior é {}'.format(m.ceil(num)))
print('O valor arredondado para o próximo menor é {}'.format(m.floor(num)))
print('O valor inteiro é {}'.format(m.trunc(num)))
