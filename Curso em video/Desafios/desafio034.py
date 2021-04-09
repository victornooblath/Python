#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("digite seu salário: "))
aumento10 = salario+(salario*10/100)
aumento15 = salario+(salario*15/100)
if salario > 1250:
    print("seu salario agora é {:.2f} reais".format(aumento10))
else:
    print("seu salario agora é de {:.2f} reais".format(aumento15))