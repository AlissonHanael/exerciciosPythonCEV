n = int(input('Digite um número para verificar sua tabuada: '))

for i in range(1, 11):
    m = n*i
    print('{} x {} = {}'.format(n, i, m))
