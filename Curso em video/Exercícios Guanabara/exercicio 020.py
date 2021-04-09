#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
n1 = str(input("Digite o primeiro nome: "))
n2 = str(input("Digite o segundo nome: "))
n3 = str(input("Digite o terceiro nome: "))
n4 = str(input("Digite o quarto nome: "))
lista = [n1,n2,n3,n4]
#o método shuffle embaralha algo dentro do parâmetro
shuffle(lista)
print("Os escolhidos foram:\n{} ".format(lista))