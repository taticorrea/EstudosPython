def maiorde3numeros():
	num1 = float(input("Digite um número: "))
	num2 = float(input("Digite um segundo  número: "))
	num3 = float(input("Digite um terceiro número: "))

	#checagem se o primeiro numero e o maior 
	if num1 > num2 and num1 > num3:
	    print("O maior número é o ",num1)
	#checagem se o segundo numero e o maior
	elif num2 > num1 and num2 > num3:
	    print("O maior número é o",num2)
	#checagem se o tercerio numero e o maior
	elif num3 > num1 and num3 > num2:
	    print("O maior número é o ",num3)

maiorde3numeros()
