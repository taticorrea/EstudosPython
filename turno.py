turno = input('Digite o turno em que você estuda (V - vespertino, M - matutino e N - noturno): ')

def functurno():
    if turno == "M":
        print('Bom dia!')
    elif turno == "V":
        print('Boa tarde!')
    elif turno == "N":
        print('Boa noite!')
    else:
        print('Turno inválido! Rode o programa novamente e insira um turno válido.')

functurno()
