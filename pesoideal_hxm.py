import numpy as np

genero = input("Digite o gênero (Feminino ou Masculino): ")
altura = float(input("Digite a altura: "))
if genero =="Feminino":
    peso_ideal = 62.1*altura - 44.7
    print("Seu peso ideal é: ", peso_ideal)
else:
    peso_ideal = 72.7*altura - 58
    print("Seu peso ideal é: ", peso_ideal)
