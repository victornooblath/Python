#Faça um algorítimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
prod = float(input('Qual o valor do produto?:'))
desconto = (5/100)+1.0
print('Seu produto com desconto saiu por {:.2f} reais'.format(prod-desconto))