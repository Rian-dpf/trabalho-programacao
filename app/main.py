from functions import *

while True:
    opc_escolhida = menuPrincipal()

    if opc_escolhida == '1':
        cadastroReservas()
            
    elif opc_escolhida == '2':
        entradaCliente()

    elif opc_escolhida == '3':
        saidaCliente()

    elif opc_escolhida == '4':
        alteracaoReserva()

    elif opc_escolhida == '5':
        relatorioReservas()

    elif opc_escolhida == '6':
        break

    else:
        print("\nDIGITE UMA OPÇÃO VÁLIDA!")