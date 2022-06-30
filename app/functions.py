import os

def menuPrincipal():
    print("\nEscolha uma das opções abaixo! \n")
    print("1 - Cadastrar uma reserva.")
    print("2 - Entrada do cliente (Check in)")
    print("3 - Saída do cliente (Check out)")
    print("4 - Alterar Reserva")
    print("5 - Relatórios")
    print("6 - Sair \n")

    opc = input("Digite a opção desejada: ")

    return opc

def validaVazio(arg1, arg2):
    if arg1 == '':
        while arg1 == '':
            print(f"{arg2} obrigatório! \n")
            arg1 = str(input(f"{arg2}: "))

    return arg1

def cadastroReservas():
    print("\nFavor preencher as informações necessárias \n")

    nome_pessoa = str(input("Nome: "))
    nome_pessoa = validaVazio(nome_pessoa, 'Nome')
    cpf = str(input("CPF: "))
    cpf = validaVazio(cpf, 'CPF')
    nr_pessoas = str(input("Número de pessoas: "))
    nr_pessoas = validaVazio(nr_pessoas, 'Número de pessoas')

    print(" \nEscolha o tipo de quarto: \n")
    print("S - Standard")
    print("D – Deluxe")
    print("P – Premium \n")

    tipo_quartos = str(input("Digite aopção desejada: "))
    tipo_quartos = validaVazio(tipo_quartos, 'Tipo de quarto')

    nr_dias = str(input("Número de dias: ")) 
    nr_dias = validaVazio(nr_dias, 'Número de dias')

    if str(tipo_quartos) == 'S':
        valor = 100 * int(nr_pessoas)
    elif str(tipo_quartos) == 'D':
        valor = 200 * int(nr_pessoas)
    else:
        valor = 300 * int(nr_pessoas)

    nr_pessoas = str(nr_pessoas) 
    valor = str(valor) 
    status = 'R \n'

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

    arquivo = open("app/reservas.txt", "a")
    arquivo.writelines(dados_reserva)
    arquivo.close()

    print("\nCadastro Realizado com sucesso !!!! \n")

def entradaCliente():

    if os.path.isfile('C:/Users/rian.firmino/Documents/Python/trabalho-programacao/app/reservas.txt'):
        cpf_cliente = str(input("Digite o CPF do cliente: ")) + ','
        novos_dados_reserva = []

        arquivo = open("app/reservas.txt", "r")
        dados_reserva = arquivo.readlines()
        arquivo.close()

        for i in dados_reserva:
            nome, cpf, nr_pessoas, tipo_quarto, nr_dias, valor, status = i.split(',')
            nome = nome + ','
            cpf = cpf + ','
            nr_pessoas = nr_pessoas + ','
            tipo_quarto = tipo_quarto + ','
            nr_dias = nr_dias + ','
            valor = valor + ','
            status = status

            if cpf_cliente == cpf and status == 'R \n':
                print("Deseja alterar o status da reserva para Ativo? \n")

                print("S - Sim")
                print("N - Não")

                opc = str(input("\nDigite aqui: "))
                if opc == 'S':
                    status = 'A \n'

                    novos_dados_reserva.append(nome)
                    novos_dados_reserva.append(cpf)
                    novos_dados_reserva.append(nr_pessoas)
                    novos_dados_reserva.append(tipo_quarto)
                    novos_dados_reserva.append(nr_dias)
                    novos_dados_reserva.append(valor)
                    novos_dados_reserva.append(status)

                    print('\nCheck-in realizado com sucesso!!')
                else:
                    novos_dados_reserva.append(nome)
                    novos_dados_reserva.append(cpf)
                    novos_dados_reserva.append(nr_pessoas)
                    novos_dados_reserva.append(tipo_quarto)
                    novos_dados_reserva.append(nr_dias)
                    novos_dados_reserva.append(valor)
                    novos_dados_reserva.append(status)

            else:

                novos_dados_reserva.append(nome)
                novos_dados_reserva.append(cpf)
                novos_dados_reserva.append(nr_pessoas)
                novos_dados_reserva.append(tipo_quarto)
                novos_dados_reserva.append(nr_dias)
                novos_dados_reserva.append(valor)
                novos_dados_reserva.append(status)

                print('\nNão encontramos este CPF na lista de reservas!')

            os.remove('app/reservas.txt')
            arquivo = open("app/reservas.txt", "a")
            arquivo.writelines(novos_dados_reserva)
            arquivo.close()
    else:
        print('Não existe nenhum cliente para dar entrada, favor realizar o cadastro!')

def saidaCliente():
    if os.path.isfile('C:/Users/rian.firmino/Documents/Python/trabalho-programacao/app/reservas.txt'):
        cpf_cliente = str(input("Digite o CPF do cliente: ")) + ','
        novos_dados_reserva = []

        arquivo = open("app/reservas.txt", "r")
        dados_reserva = arquivo.readlines()
        arquivo.close()

        for i in dados_reserva:
            nome, cpf, nr_pessoas, tipo_quarto, nr_dias, valor, status = i.split(',')
            nome = nome + ','
            cpf = cpf + ','
            nr_pessoas = nr_pessoas + ','
            tipo_quarto = tipo_quarto + ','
            nr_dias = nr_dias + ','
            valor = valor + ','
            status = status

            if cpf_cliente == cpf and status == 'A \n':
                print("Deseja realizar o check-out deste cliente? \n")

                print("S - Sim")
                print("N - Não")

                opc = str(input("\nDigite aqui: "))
                if opc == 'S':
                    status = 'F \n'

                    novos_dados_reserva.append(nome)
                    novos_dados_reserva.append(cpf)
                    novos_dados_reserva.append(nr_pessoas)
                    novos_dados_reserva.append(tipo_quarto)
                    novos_dados_reserva.append(nr_dias)
                    novos_dados_reserva.append(valor)
                    novos_dados_reserva.append(status)

                    print('Check-out realizado com sucesso!')
                else:
                    novos_dados_reserva.append(nome)
                    novos_dados_reserva.append(cpf)
                    novos_dados_reserva.append(nr_pessoas)
                    novos_dados_reserva.append(tipo_quarto)
                    novos_dados_reserva.append(nr_dias)
                    novos_dados_reserva.append(valor)
                    novos_dados_reserva.append(status)
            else:

                novos_dados_reserva.append(nome)
                novos_dados_reserva.append(cpf)
                novos_dados_reserva.append(nr_pessoas)
                novos_dados_reserva.append(tipo_quarto)
                novos_dados_reserva.append(nr_dias)
                novos_dados_reserva.append(valor)
                novos_dados_reserva.append(status)

                print('\nNão encontramos este CPF na lista de reservas! \n')

            os.remove('app/reservas.txt')
            arquivo = open("app/reservas.txt", "a")
            arquivo.writelines(novos_dados_reserva)
            arquivo.close()
    else:
        print('Não existe nenhum cliente para dar saída, favor realizar o cadastro!')

def alteracaoReserva():
    if os.path.isfile('C:/Users/rian.firmino/Documents/Python/trabalho-programacao/app/reservas.txt'):
        cpf_cliente = str(input("Digite o CPF do cliente: ")) + ','
        novos_dados_reserva = []

        arquivo = open("app/reservas.txt", "r")
        dados_reserva = arquivo.readlines()
        arquivo.close()

        for i in dados_reserva:
            nome, cpf, nr_pessoas, tipo_quarto, nr_dias, valor, status = i.split(',')

            nome = nome + ','
            cpf = cpf + ','
            nr_pessoas = nr_pessoas + ','
            tipo_quarto = tipo_quarto + ','
            nr_dias = nr_dias + ','
            valor = valor + ','
            status = status

            if cpf_cliente == cpf:
                nr_pessoas = str(input("Novo número de pessoas: "))
                while nr_pessoas == '':
                    print(f"A informação do Número de pessoas é obrigatória! \n")
                    nr_pessoas = str(input("Número de pessoas: "))

                print(" \nEscolha o tipo de quarto: \n")
                print("S - Standard")
                print("D – Deluxe")
                print("P – Premium \n")

                tipo_quarto = str(input("Digite aopção desejada: "))  + ','
                while tipo_quarto == '':
                    print(f"A informação do Tipo de quarto é obrigatória! \n")
                    tipo_quarto = str(input("Digite aopção desejada: ")) + ','

                nr_dias = str(input("Número de dias: ")) + ','
                while nr_dias == '':
                    print(f"A informação do número de dias é obrigatória! \n")
                    nr_dias = str(input("Número de dias: ")) + ','

                if str(tipo_quarto) == 'S':
                    valor = 100 * int(nr_pessoas)
                elif str(tipo_quarto) == 'D':
                    valor = 200 * int(nr_pessoas)
                else:
                    valor = 300 * int(nr_pessoas)

                nr_pessoas = str(nr_pessoas) + ','
                valor = str(valor) + ','

                print('\nAlterar o status para? \n')

                print('R - Reservado')
                print('C - Cancelado')
                print('A - Ativo')
                print('F - Finalizado \n')
                
                status = str(input("Digite aqui o status: ")) + ' \n'

                novos_dados_reserva.append(nome)
                novos_dados_reserva.append(cpf)
                novos_dados_reserva.append(nr_pessoas)
                novos_dados_reserva.append(tipo_quarto)
                novos_dados_reserva.append(nr_dias)
                novos_dados_reserva.append(str(valor))
                novos_dados_reserva.append(status)

                print('\nReserva alterada com sucesso!')
            else:
                novos_dados_reserva.append(nome)
                novos_dados_reserva.append(cpf)
                novos_dados_reserva.append(nr_pessoas)
                novos_dados_reserva.append(tipo_quarto)
                novos_dados_reserva.append(nr_dias)
                novos_dados_reserva.append(str(valor))
                novos_dados_reserva.append(status)

                print('\nNão encontramos este CPF na lista de reservas! \n')

        os.remove('app/reservas.txt')
        arquivo = open("app/reservas.txt", "a")
        arquivo.writelines(novos_dados_reserva)
        arquivo.close()
    else:
        print('Não existe nenhum cliente para alterar reserva, favor realizar o cadastro!')

def menuRelatorios():
    print("\n1 - Relatório de todas as reservas com status R")
    print("2 - Relatório de todas as reservas com status C")
    print("3 - Relatório de todas as reservas com status A")
    print("4 - Relatório de todas as reservas com status F")
    print("5 - Relatório total recebido (somar valor de todas as reservas finalizadas")
    print("6 – Relatório de Reserva por pessoa (Pesquisa por CPF) \n")

    opc = input("Digite a opção desejada: ")

    return opc

def relatorioReservas():
    if os.path.isfile('C:/Users/rian.firmino/Documents/Python/trabalho-programacao/app/reservas.txt'):
        opc_escolhida = menuRelatorios()

        if opc_escolhida == '1':
            arquivo = open("app/reservas.txt", "r")
            dados_reserva = arquivo.readlines()
            arquivo.close()

            lista_reservas_status_r = []

            for i in dados_reserva:
                nome, cpf, nr_pessoas, tipo_quarto, nr_dias, valor, status = i.split(',')
                nome = nome + ','
                cpf = cpf + ','
                nr_pessoas = nr_pessoas + ','
                tipo_quarto = tipo_quarto + ','
                nr_dias = nr_dias + ','
                valor = valor + ','
                status = status

                if status == 'R \n':
                    lista_reservas_status_r.append(nome)
                    lista_reservas_status_r.append(cpf)
                    lista_reservas_status_r.append(nr_pessoas)
                    lista_reservas_status_r.append(tipo_quarto)
                    lista_reservas_status_r.append(nr_dias)
                    lista_reservas_status_r.append(valor)
                    lista_reservas_status_r.append(status)
                else:
                    pass

            if os.path.isfile('C:/Users/rian.firmino/Documents/Python/trabalho-programacao/relatorios/relatorio_reservas_realizadas.txt'):
                os.remove('relatorios/relatorio_reservas_realizadas.txt')
                arquivo = open("relatorios/relatorio_reservas_realizadas.txt", "a")
                arquivo.writelines(lista_reservas_status_r)
                arquivo.close()
            else:
                arquivo = open("relatorios/relatorio_reservas_realizadas.txt", "a")
                arquivo.writelines(lista_reservas_status_r)
                arquivo.close()

        elif opc_escolhida == '2':
            arquivo = open("app/reservas.txt", "r")
            dados_reserva = arquivo.readlines()
            arquivo.close()

            lista_reservas_status_c = []

            for i in dados_reserva:
                nome, cpf, nr_pessoas, tipo_quarto, nr_dias, valor, status = i.split(',')
                nome = nome + ','
                cpf = cpf + ','
                nr_pessoas = nr_pessoas + ','
                tipo_quarto = tipo_quarto + ','
                nr_dias = nr_dias + ','
                valor = valor + ','
                status = status

                if status == 'C \n':
                    lista_reservas_status_c.append(nome)
                    lista_reservas_status_c.append(cpf)
                    lista_reservas_status_c.append(nr_pessoas)
                    lista_reservas_status_c.append(tipo_quarto)
                    lista_reservas_status_c.append(nr_dias)
                    lista_reservas_status_c.append(valor)
                    lista_reservas_status_c.append(status)
                else:
                    pass

            if os.path.isfile('C:/Users/rian.firmino/Documents/Python/trabalho-programacao/relatorios/relatorio_reservas_canceladas.txt'):
                os.remove('relatorios/relatorio_reservas_canceladas.txt')
                arquivo = open("relatorios/relatorio_reservas_canceladas.txt", "a")
                arquivo.writelines(lista_reservas_status_c)
                arquivo.close()
            else:
                arquivo = open("relatorios/relatorio_reservas_canceladas.txt", "a")
                arquivo.writelines(lista_reservas_status_c)
                arquivo.close()

        elif opc_escolhida == '3':
            arquivo = open("app/reservas.txt", "r")
            dados_reserva = arquivo.readlines()
            arquivo.close()

            lista_reservas_status_a = []

            for i in dados_reserva:
                nome, cpf, nr_pessoas, tipo_quarto, nr_dias, valor, status = i.split(',')
                nome = nome + ','
                cpf = cpf + ','
                nr_pessoas = nr_pessoas + ','
                tipo_quarto = tipo_quarto + ','
                nr_dias = nr_dias + ','
                valor = valor + ','
                status = status

                if status == 'A \n':
                    lista_reservas_status_a.append(nome)
                    lista_reservas_status_a.append(cpf)
                    lista_reservas_status_a.append(nr_pessoas)
                    lista_reservas_status_a.append(tipo_quarto)
                    lista_reservas_status_a.append(nr_dias)
                    lista_reservas_status_a.append(valor)
                    lista_reservas_status_a.append(status)
                else:
                    pass
        
            if os.path.isfile('C:/Users/rian.firmino/Documents/Python/trabalho-programacao/relatorios/relatorio_reservas_ativas.txt'):
                os.remove('relatorios/relatorio_reservas_ativas.txt')
                arquivo = open("relatorios/relatorio_reservas_ativas.txt", "a")
                arquivo.writelines(lista_reservas_status_a)
                arquivo.close()
            else:
                arquivo = open("relatorios/relatorio_reservas_ativas.txt", "a")
                arquivo.writelines(lista_reservas_status_a)
                arquivo.close()

        elif opc_escolhida == '4':
            arquivo = open("app/reservas.txt", "r")
            dados_reserva = arquivo.readlines()
            arquivo.close()

            lista_reservas_status_f = []

            for i in dados_reserva:
                nome, cpf, nr_pessoas, tipo_quarto, nr_dias, valor, status = i.split(',')
                nome = nome + ','
                cpf = cpf + ','
                nr_pessoas = nr_pessoas + ','
                tipo_quarto = tipo_quarto + ','
                nr_dias = nr_dias + ','
                valor = valor + ','
                status = status

                if status == 'F \n':
                    lista_reservas_status_f.append(nome)
                    lista_reservas_status_f.append(cpf)
                    lista_reservas_status_f.append(nr_pessoas)
                    lista_reservas_status_f.append(tipo_quarto)
                    lista_reservas_status_f.append(nr_dias)
                    lista_reservas_status_f.append(valor)
                    lista_reservas_status_f.append(status)
                else:
                    pass
        
            if os.path.isfile('C:/Users/rian.firmino/Documents/Python/trabalho-programacao/relatorios/relatorio_reservas_finalizadas.txt'):
                os.remove('relatorios/relatorio_reservas_finalizadas.txt')
                arquivo = open("relatorios/relatorio_reservas_finalizadas.txt", "a")
                arquivo.writelines(lista_reservas_status_f)
                arquivo.close()
            else:
                arquivo = open("relatorios/relatorio_reservas_finalizadas.txt", "a")
                arquivo.writelines(lista_reservas_status_f)
                arquivo.close()

        elif opc_escolhida == '5':
            arquivo = open("app/reservas.txt", "r")
            dados_reserva = arquivo.readlines()
            arquivo.close()

            total_recebido = []

            for i in dados_reserva:
                nome, cpf, nr_pessoas, tipo_quarto, nr_dias, valor, status = i.split(',')

                if status == 'F \n':
                    total_recebido.append(int(valor))
                else:
                    pass
            total = sum(total_recebido)   

            if os.path.isfile('C:/Users/rian.firmino/Documents/Python/trabalho-programacao/relatorios/relatorio_total_recebido.txt'):
                os.remove('relatorios/relatorio_total_recebido.txt')
                arquivo = open("relatorios/relatorio_total_recebido.txt", "a")
                arquivo.writelines(F'A soma de todas as reservas finalizadas da um total de: {str(total)} R$')
                arquivo.close()
            else:
                arquivo = open("relatorios/relatorio_total_recebido.txt", "a")
                arquivo.writelines(F'A soma de todas as reservas finalizadas da um total de: {str(total)} R$')
                arquivo.close()

        elif opc_escolhida == '6':
            cpf_cliente = str(input("Digite o CPF do cliente: ")) + ','
            reserva_por_pessoa = []

            arquivo = open("app/reservas.txt", "r")
            dados_reserva = arquivo.readlines()
            arquivo.close()

            for i in dados_reserva:
                nome, cpf, nr_pessoas, tipo_quarto, nr_dias, valor, status = i.split(',')
                nome = nome + ','
                cpf = cpf + ','
                nr_pessoas = nr_pessoas + ','
                tipo_quarto = tipo_quarto + ','
                nr_dias = nr_dias + ','
                valor = valor + ','
                status = status

                if cpf_cliente == cpf:
                        reserva_por_pessoa.append(nome)
                        reserva_por_pessoa.append(cpf)
                        reserva_por_pessoa.append(nr_pessoas)
                        reserva_por_pessoa.append(tipo_quarto)
                        reserva_por_pessoa.append(nr_dias)
                        reserva_por_pessoa.append(valor)
                        reserva_por_pessoa.append(status)

            if os.path.isfile('C:/Users/rian.firmino/Documents/Python/trabalho-programacao/relatorios/relatorio_reserva_por_pessoa.txt'):
                os.remove('relatorios/relatorio_reserva_por_pessoa.txt')
                arquivo = open("relatorios/relatorio_reserva_por_pessoa.txt", "a")
                arquivo.writelines(reserva_por_pessoa)
                arquivo.close()
            else:
                arquivo = open("relatorios/relatorio_reserva_por_pessoa.txt", "a")
                arquivo.writelines(reserva_por_pessoa)
                arquivo.close()

        else:
            print('\nDigite uma opção válida! \n')
            menuRelatorios()

    else:
        print('Não existe nenhum cliente para emitir relatórios, favor realizar o cadastro!')
