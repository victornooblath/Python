# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
nMET= int(input('Digite um número em metros:'))
nCEM= nMET*100
nMM= nMET*1000
print('O valor em metro é:{}\n O valor em Cm é:{}\n O valor em Mm é:{}'.format(nMET,nCEM,nMM))