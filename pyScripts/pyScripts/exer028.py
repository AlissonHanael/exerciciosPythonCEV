import random as r
print('ADIVINHA O NUMERO!!')
num = r.randint(1, 5)
print(num)
numDigitado = int(
    input('Digite um numero e tente acertar qual o computador gerou (1 a 5): '))
if num == numDigitado:
    print('Você acertou!')
else:
    print('Você errou :(')
