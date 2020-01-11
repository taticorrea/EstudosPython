import numpy as np 

area = float(input("Digita a área, em m², a ser pintada: "))
qtd_litros = area/3
qtd_latas = qtd_litros//18 + 1
custo = 80*qtd_latas

print("Serão necessários",qtd_litros,"litros de tinta para pintar os",area,"m²")
print("A quantidade de latas necessárias será: ",qtd_latas)
print("O custo total será de: R$", custo)

