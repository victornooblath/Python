#Faça um algorítimo que leia um salário e mostre seu novo salário , com 15% de aumento
salário = float(input('Qual o valor do salário?:'))
aumento = salário*(15/100)
print('Seu salário após o aumento saiu por {:.2f} reais'.format(salário+aumento))