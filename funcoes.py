import os

def menuPrincipal():
    print("Escolha uma das opções abaixo! \n")
    print("1 - Cadastrar uma reserva.")
    print("2 - Entrada do cliente (Check in)")
    print("3 - Saída do cliente (Check out)")
    print("4 - Alterar Reserva")
    print("5 - Relatórios")
    print("6 - Sair \n")

    opc = int(input("Digite a opção desejada: "))

    return opc

def cadastroReservas():
    print("\nFavor preencher as informações necessárias \n")

    nome_pessoa = str(input("Nome: "))

    while nome_pessoa == '':
        print(f"A informação do nome é obrigatória! \n")
        nome_pessoa = str(input("Nome: "))

    cpf = str(input("CPF: "))

    while cpf == '':
        print(f"A informação do CPF é obrigatória! \n")
        cpf = str(input("CPF: "))

    nr_pessoas = str(input("Número de pessoas: "))

    while nr_pessoas == '':
        print(f"A informação do Número de pessoas é obrigatória! \n")
        nr_pessoas = str(input("Número de pessoas: "))


    print(" \nEscolha o tipo de quarto: \n")
    print("S - Standard")
    print("D – Deluxe")
    print("P – Premium \n")

    tipo_quartos = str(input("Digite aopção desejada: "))

    while tipo_quartos == '':
        print(f"A informação do Tipo de quarto é obrigatória! \n")
        tipo_quartos = str(input("Digite aopção desejada: "))


    nr_dias = str(input("Número de dias: "))

    while nr_dias == '':
        print(f"A informação do número de dias é obrigatória! \n")
        nr_dias = str(input("Número de dias: "))

    if str(tipo_quartos) == 'S':
        valor = 100 * int(nr_pessoas)
    elif str(tipo_quartos) == 'D':
        valor = 200 * int(nr_pessoas)
    else:
        valor = 300 * int(nr_pessoas)

    status = 'R'

    dados_reserva = []

    dados_reserva.append(nome_pessoa)
    dados_reserva.append(',')
    dados_reserva.append(cpf)
    dados_reserva.append(',')
    dados_reserva.append(nr_pessoas)
    dados_reserva.append(',')
    dados_reserva.append(tipo_quartos)
    dados_reserva.append(',')
    dados_reserva.append(nr_dias)
    dados_reserva.append(',')
    dados_reserva.append(str(valor))
    dados_reserva.append(',')
    dados_reserva.append(status)
    dados_reserva.append('\n')

    arquivo = open("reservas.txt", "a")
    arquivo.writelines(dados_reserva)
    arquivo.close()

    print("\nCadastro Realizado com sucesso !!!! \n")

def entradaCliente():
    cpf_cliente = str(input("Digite o CPF do cliente: "))
    lista_nova = []

    arquivo = open("reservas.txt", "r")
    dados_reserva = arquivo.readlines()
    arquivo.close()

    for i in dados_reserva:
        dados_reserva_lista = i.split(',')

        if cpf_cliente in dados_reserva_lista:
            print("Deseja alterar o status da reserva para Ativo? \n")

            print("S - Sim")
            print("N - Não")

            opc = str(input("\nDigite aqui: "))
            if opc == 'S':
                dados_reserva_lista[-1] = 'A'
                lista_nova.append(dados_reserva_lista)

        else:
            lista_nova.append(dados_reserva_lista)

    nova_lista = []

    for i in lista_nova[0]:
        nova_lista.append(i)
        nova_lista.append(',')

    nova_lista.append('\n')

    for i in lista_nova[1]:
        nova_lista.append(i)
        nova_lista.append(',')

    os.remove('reservas.txt')
    
    arquivo = open("reservas.txt", "a")
    arquivo.writelines(nova_lista)
    arquivo.close()