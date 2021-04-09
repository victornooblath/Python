#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra
# “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input("digite uma frase: ")).upper()
print("A quantidade de letras 'a' contidas na frase são {} ".format(frase.count('A')))
print("A primeira letra 'a' foi encontrada na posição {}\nE a ultima letra a"
      "foi achada na posição {} ".format(frase.find('A')+1,frase.rfind('A')+1))
