#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = int(input("Digite um numero :"))
n = str(numero)
print("Unidade:{}\nDezena:{}\nCentena:{}\nMilhar:{} ".format(n[3],n[2],n[1],n[0]))
