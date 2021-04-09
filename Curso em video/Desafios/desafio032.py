#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano= int(input("digite um Ano|Caso voce queira analisar o ano atual digite 0: "))
if ano== 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print("{} Ele é bissexto".format(ano))
else:
    print("{} não é bissexto".format(ano))
