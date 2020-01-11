import numpy as np

nota1 = input('Digite a primeira nota: ')
nota2 = input("Digite a segunda nota: ")
nota3 = input("Digite a terceira nota: ")
nota4 = input("Digite a quarta nota: ")
n = [int(nota1),int(nota2),int(nota3),int(nota4)]
media = np.median(n)
print("As notas foram: ", n,"\nA média é: ", media)
