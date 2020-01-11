tam = float(input("Digite o tamanho do arquivo, em MB.: "))
vel = float(input("Digite a velocidade de download, em Mbps: "))
t_seg = float(tam/vel)
t_min =float( (tam/vel)/60)
print("O tempo aproximado de download do arquivo é: ",t_seg,"segundos.")
print("O tempo aproximado de download do arquivo é: ",t_min,"minutos.")

