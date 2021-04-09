#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#considerando que o dólar é 5,67
carteira = float(input('Quantos reais você tem na carteira?:'))
print('Com R${} reais você pode comprar {:.0f} dólares '.format(carteira,carteira//5,67))