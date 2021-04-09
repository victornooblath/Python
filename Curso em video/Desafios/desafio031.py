#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
#cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
kmrod = float(input("Quantos km rodado?"))
if kmrod<=200:
    print("A viagem custou {:.2f} reais".format(kmrod*0.50))
else:
    print("A viagem custou {:.2f} reais".format(kmrod*0.45))