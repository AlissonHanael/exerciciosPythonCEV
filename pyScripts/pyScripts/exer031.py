print('Calculadora de viagens para viagens de até 200km o valor é 0.50/km\nPara viagens mais longas 0.45/km')
km = float(input('Digite a distancia em km: '))
if km <= 200 and km > 0:
    print('Valor total da viagem: R${}'.format(km*0.5))
else:
    print('Valor total da viagem: R${}'.format(km*0.45))
