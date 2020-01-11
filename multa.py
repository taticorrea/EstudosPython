import numpy as np

quantidade = float(input("Digite a quantidade, em kg, de peixe: "))
if quantidade > 50:
    excesso = quantidade - 50 
    multa = excesso*4
    print("O excesso foi de: ",excesso,"kg")
    print("O valor da multa é: R$",multa)
else:
    print("Não há multa a pagar")
