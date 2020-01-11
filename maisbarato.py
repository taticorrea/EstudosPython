preco1 = float(input("Digite o preço do primeiro produto: R$"))
preco2 = float(input("Digite o preço do segundo produto: R$"))
preco3 = float(input("Digite o preço do terceiro produto: R$"))
if preco1 < preco2 and preco1 < preco3:
    print("O produto mais barato é o ",preco1)
elif preco2 < preco1 and preco2 < preco3:
    print("O produto mais barato é o ",preco2)
elif preco3 < preco1 and preco3 < preco2:
    print("O produto mais barato é o ",preco3)
