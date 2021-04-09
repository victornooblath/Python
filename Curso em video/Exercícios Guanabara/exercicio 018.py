#Crie um programa que ele pede um angulo, e o python calcula o seno,cosseno e tangente
from math import sin,cos,tan,radians
ângulo = float(input("Digite um ângulo: "))
#O seno precisa estar em radiano, então dentro do método sin eu ponho o radians para conversão direta
seno= sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print("O valor do seno é {:.2f}\nO valor do cosseno é {:.2f}\nO valor da tangente é {:.2f}".format(seno,cosseno,tangente))