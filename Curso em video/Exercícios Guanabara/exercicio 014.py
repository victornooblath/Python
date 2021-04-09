#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = int(input('Qual a temperatura em celsius?:'))
fahrenheit = (celsius*1.8)+32
print('A temperatura em Fahrenheit é {:.1f}'.format(fahrenheit))