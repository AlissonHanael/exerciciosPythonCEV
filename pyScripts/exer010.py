print('Conversor de money!\nVerifique quantos dólares ou euros você pode comprar!')
mon = float(input('Digite quanto você tem em reais: R$'))
dol = mon/5.40
eur = mon/6.21
print(
    'Você pode comprar: US${:.2f}\nVocê pode comprar: €${:.2f}'.format(dol, eur))
