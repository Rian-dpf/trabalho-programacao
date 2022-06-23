from functions import *

while True:
    opc_escolhida = menuPrincipal()

    if opc_escolhida == 1:
        cadastroReservas()
            
    elif opc_escolhida == 2:
        entradaCliente()