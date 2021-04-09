#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
kmrod= float(input("Quantos km vc rodou?: "))
if kmrod > 80.0:
    print("limite ultrapassado, a multa foi de {:.2f} reais ".format((kmrod-80)*7))
else:
    print("Continue")