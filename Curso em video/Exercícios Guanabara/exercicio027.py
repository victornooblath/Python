#Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.
nome= str(input("digite seu nome: ")).strip().title().split()
print("seu primeiro nome é {}\nSeu ultimo nome é {}".format(nome[0],nome[len(nome)-1]))