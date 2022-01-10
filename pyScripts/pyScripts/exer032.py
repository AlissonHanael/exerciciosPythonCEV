from datetime import date
print('Descubra se o ano é bissexto, se voce quiser analisar o ano atual digite 0')
ano = int(input('Digite o ano que voce quer analisar: (0 para o ano atual)'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
