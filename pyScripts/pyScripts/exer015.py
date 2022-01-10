print('----Aluguel de Carros----')
km = int(input('insira a quantidade de KMs rodados: '))
days = int(input('insira a quantidade de dias que ele foi alugado: '))
valorDia = 60*days
valorKm = 0.15*km
valorTotal = valorDia + valorKm
print('---------')
print('O valor total do aluguel do veículo é: R${:.2f}'.format(valorTotal))
