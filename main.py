from contagem_dias import contagem_dias
from leitor_de_arquivos import leitor_de_arquivos
from funcao_transforma import transforma_em_data

print("\nBem vindo ao contador_de_dias.py, siga as instruções a seguir.\n")

while True:
    print("Se você deseja inserir as datas manualmente, digite 1. \nSe você deseja inserir o caminho de um arquivo com as datas, digite 2.\n")
    comando = input("Qual a sua escolha? ")

    if comando == "1":
        print("\nInsira as duas datas. Ex.: 28 de Agosto de 2023 - 18 de Setembro de 2023.")
        datas = input("Insira aqui:")
        break
    elif comando == "2":
        print("\nInsira o caminho do arquivo de texto. Ele deve conter apenas uma linha com as datas.")
        caminho = input("Insira aqui: ")
        datas = leitor_de_arquivos(caminho)
        break
    else:
        print("\n--> Valor inválido. Insira 1 ou 2. <--\n")

datas = datas.split(" - ")

data_1 = transforma_em_data(datas[0])
data_2 = transforma_em_data(datas[1])

dias = contagem_dias(data_1, data_2)

print("Número de dias entre as datas:", dias)