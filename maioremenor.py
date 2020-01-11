def maioremenor():
	num1 = float(input("Digite um primeiro número: "))
	num2 = float(input("Digite um segundo número: "))
	num3 = float(input("Digite um terceiro número: "))
	if num1 > num2 and num2 > num3:
	    print("O maior número é o",num1,"\n O menor número é o ",num3)
	elif num1 > num2 and num3 > num2:
	    print("O maior número é o ",num1,"\n O menor número é o ",num2)

	elif num2 > num1 and num1 > num3:
	    print("O maior número é o ",num2,"\n O menor número é o ",num3)
	elif num2 > num1 and num3 > num1:
	    print("O maior número é o ",num2,"\n O menor número é o ",num1)

	elif num3 > num1 and num1 > num2:
	    print("O maior número é o ",num3,"\n O menor número é o ",num2)
	elif num3 > num1 and num2 > num1:
	    print("O maior número é o ",num3,"\n O menor número é o ",num1)

maioremenor()
