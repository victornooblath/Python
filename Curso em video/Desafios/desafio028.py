#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from numpy.random.mtrand import randint
chute = int(input("chuta um numero mlk de 1 ate 5:"))
n = randint(1,5)
print("o numero foi {}".format(n))
print("acerto miseravi" if n == chute else "errou")

