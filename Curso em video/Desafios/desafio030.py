#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input("digite um número: "))
print("{} é um numero par".format(n) if n%2==0 else "ele é impar")