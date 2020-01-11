import numpy as np

horas = int(input("Digite a quantidade de horas trabalhadas no mês :"))
valor = int(input("Digite o valor da sua hora de trabalho: "))
salario = horas*valor
print("O valor recebido no mês por ",horas," horas de trabalho será de: R$",salario," reais")
