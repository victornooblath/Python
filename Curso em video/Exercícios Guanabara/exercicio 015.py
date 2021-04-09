#screva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = int(input('Digite quantos km o veiculo rodou:'))
dia = int(input('Digite o número de dias que o veiculo rodou:'))
km_rod= km*0.15
dia_cons = dia*60
print('O aluguel do carro foi de R${:.1f} reais'.format(km_rod+dia_cons))