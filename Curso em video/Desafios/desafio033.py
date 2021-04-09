# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input("digite o numero 1: "))
b = int(input("Digite o numero 2: "))
c = int(input("Digite o numero 3: "))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("o menor é {} e o maior é {} ".format(menor, maior))
