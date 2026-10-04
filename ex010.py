real = float(input('Quanto dinheiro você tem na sua carteira? R$'))
dolar = real / 5.21
print('Com R${:.2f} você consegue comprar US${:.2f}.'.format(real, dolar))
