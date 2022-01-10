print('*--*'*20)
print('*--*'*8 + 'RADAR ELETRONICO' + '*--*'*8)
print('*--*'*20)
vel = int(input('Digite a velocidade do veiculo: '))
if vel > 80:
    multa = (vel - 80)*7
    print('Você foi multado!!\nValor da multa: R${}'.format(multa))
else:
    print('Você não foi multado, siga sua viagem com cuidado :)')
