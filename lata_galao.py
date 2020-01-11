import numpy as np

area = float(input("Digite o valor da área, em m², a ser pintada: "))
qtd_litros = area/6
qtd_latas = qtd_litros//18 + 1
qtd_latas1 = int(qtd_litros/18)
qtd_galao1 = qtd_latas1//3.6 + 1
qtd_galoes = qtd_litros//3.6 + 1
custo_lata = qtd_latas*80
custo_galao = qtd_galoes*25
custo_total = qtd_latas1*80 + qtd_galao1*25
print("Serão necessários",qtd_litros,"litros de tinta para pintar os",area,"m²")
print("Comprando apenas latas de tinta de 18L, a quantidade necessárias será de: ",qtd_latas,"latas.\nCom um custo total de: R$",custo_lata)
print("Comprando apenas galões de tinta de 3.6L, a quantidade necessária será de: ",qtd_galoes,"galões.\nCom um custo total de: R$",custo_galao)
print("Comprando galões e latas de tinta, de forma que a reduzir o custo, serão",qtd_latas1,"latas e ",qtd_galao1,"galões.\nCom um custo total de: R$",custo_total)
