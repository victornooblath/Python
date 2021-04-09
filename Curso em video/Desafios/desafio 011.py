#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
#para pintála, sabendo que cada litro de tinta, pinta uma área de 2m²
altura= float(input('Informe a altura da parede:'))
largura= float(input('Informe a largura da parede:'))
area = altura*largura
print('Você irá precisar de {:.1f} litros de tinta'.format(area/2))