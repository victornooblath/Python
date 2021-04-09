"""Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome 40040104."""""

nome = str(input("Qual seu nome?")).strip()
print("seu nome completo em maiúsculo é: {}\nSeu nome em minúscula é: {}".format(nome.upper(),nome.lower()))
print("Possui no total de {} caracteres, sendo o inicial com: "
      "{} caracteres".format(len(nome) - nome.count(' '), nome.find(' ')))

