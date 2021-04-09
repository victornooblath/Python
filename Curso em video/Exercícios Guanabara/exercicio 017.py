#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input("Qual o comprimento do cateto oposto?: "))
ca = float(input("qual o comprimento do cateto adjacente?: "))
hi = hypot(co,ca)
print("O valor da hipotenusa é: {:.2f} ".format(hi))
