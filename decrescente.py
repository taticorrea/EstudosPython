num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número:'))
num3 = float(input('Digite o terceiro número: '))

#Ordem descrescente 

#Comparando o terceiro com o segundo
if num3 > num2:
    aux = num3
    num3 = num2
    num2 = aux

#Comparando o segundo com o primeiro
if num2 > num1:
    aux = num2
    num2 = num1
    num1 = aux

#Comparando o terceiro com o segundo novamente    
if num3 > num2:
    aux = num3
    num3 = num2
    num2 = aux

print (num1,'|',num2,'|',num3)
