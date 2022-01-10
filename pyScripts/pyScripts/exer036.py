valorCasa = float(input('Digite o valor da casa que você deseja comprar: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
ano = int(input('Digite em quantos anos você quer pagar: '))
parcela = valorCasa/(ano*12)
if parcela > (salario*0.3):
    print('Empréstimo negado')
else:
    print('Empréstimo aceito')
