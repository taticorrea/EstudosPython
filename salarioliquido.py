import numpy as np

salario_hora = float(input("Digite o valor da sua hora de trabalho: R$"))
horas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = salario_hora*horas
ir = 0.11*salario_bruto
inss = 0.08*salario_bruto
sindicato = 0.05*salario_bruto
descontos = ir + inss + sindicato

salario_liquido = salario_bruto - descontos

print("+ Salário Bruto: R$",salario_bruto)
print("- IR: R$",ir)
print("- INSS: R$",inss)
print("- Sindicato: R$",sindicato)
print("= Salário Líquido: R$",salario_liquido)

