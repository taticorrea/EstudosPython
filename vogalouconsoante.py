def vogalouconsoante():
	vogais = ["a","e","i","o","u"]
	consoantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
	letra = input("Digite uma letra: ")
	if letra in vogais:
	    print("A letra",letra,"é uma vogal")
	elif letra in consoantes:
	    print("A letra",letra,"é uma consoante")
	else:
	    print("Digite uma letra ao invés de um número")	

vogalouconsoante()
