#Faça um programa que leia um número inteiro qualquer e mostre a sua tabuada
aleat = int(input('Digite um número:'))
print('A taboada de {} é:'.format(aleat))
for i in range(11):
    print('{} x {} = {}'.format(i,aleat,aleat*i))