def salario():
    salario = float(input('Digite seu salário: R$'))
    print('Os reajustes seguem o seguinte critério:\nSalário < R$280,00 -> 20% de aumento\nR280,00 < Salário < R$700,00 ->15% de aumento\nR$700,00 < Salário < R$1500,00 -> 10% de aumento\nSalário > R$1500,00 -> 5% de aumento')
    if salario < 280.00:
        percentual = '20%'
        aumento = 0.2*salario
        novo_salario = salario + aumento
        print('\nO seu salario antes do reajuste era: R$',salario,'\nO percentual de aumento aplicado foi de:',percentual,'\nO valor de aumento aplicado foi de: R$',aumento,'\nO novo salário é de: R$',novo_salario)

    if 280 < salario < 700:
        percentual = '15%'
        aumento = 0.15*salario
        novo_salario = salario + aumento
        print('\nO seu salário antes do reajuste era: R$',salario,'\nO percentual de aumento aplicado foi de:',percentual,'\nO valor do aumento aplicado foi de: R$',aumento,'\nO novo salário é: R$',novo_salario)

    if 700 < salario < 1500:
        percentual = '10%'
        aumento = 0.1*salario
        novo_salario = salario + aumento
        print('\nO seu salário antes do reajuste era: R$',salario,'\nO percentual de aumento aplicado foi de:',percentual,'\nO valor do aumento aplicado foi de: R$',aumento,'\nO novo salário é: R$',novo_salario)

    if salario > 1500:
        percentual = '5%'
        aumento = 0.05*salario
        novo_salario = salario + aumento
        print('\nO seu salário antes do reajuste era: R$',salario,'\nO percentual de aumento aplicado foi de:',percentual,'\nO valor do aumento aplicado foi de: R$',aumento,'\nO novo salário é de: R$',novo_salario)

salario()
