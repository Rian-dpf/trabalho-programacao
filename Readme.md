# Equipe:
Rian, Pedro Henrique Hahn e Hebrom

# Projeto
Para a projeto final da disciplina de Programação, a equipe (no máximo 3 alunos) deverá
desenvolver um sistema para um hotel. O programa deverá ser desenvolvido na linguagem de
programação Python. O programa desenvolvido deverá cumprir as seguintes tarefas:

● Menu principal

O usuário deverá ter acesso a um menu principal com as seguintes opções:

    ▪ 1 - Cadastrar uma reserva.
    ▪ 2 - Entrada do cliente (Check in).
    ▪ 3 - Saída do cliente (Check out).
    ▪ 4 - Alterar reserva.
    ▪ 5 - Relatórios.
    ▪ 6 - Sair

O programa só deverá ser encerrado caso o usuário escolha a opção 6 - Sair.

● Cadastro de Reservas

    o Nessa tela o usuário terá a opção de cadastrar uma reserva para um cliente.
    o As informações para cadastro são:
    ▪ Nome da pessoa Titular
    ▪ CPF
    ▪ Número de pessoas
    ▪ Tipo do Quarto ( S – Standar, D – Deluxe, P – Premium)
    ▪ Número de dias
    ▪ Valor (Quarto S -> 100 por pessoa, D –> 200 por pessoa, P-> 300 por
    pessoa) por diária.
    ▪ Status (R - Reservado, C – Cancelado, A – Ativo, F - Finalizado) – No
    cadastro colocado automático como R.

Os campos considerados obrigatórios são:

    ▪ Nome da pessoa Titular
    ▪ CPF
    ▪ Número de pessoas
    ▪ Tipo do Quarto ( S – Standar, D – Deluxe, P – Premium)
    ▪ Número de dias
    ▪ Valor (Já que é calculador de forma automática)

Caso algum dos campos considerados obrigatórios não forem fornecidos, o
sistema deverá apresentar uma mensagem de aviso e reiniciar o cadastro.
o O sistema deverá apresentar mensagem de realização de cadastro com
sucesso, ex: ‘Cadastro Realizado com sucesso !!!! ’.

● Entrada do cliente (Check in).

    o Nessa tela o usuário terá a opção de dar a entrada de um cliente no hotel, ou
    seja, realizar o check in.
    o Para isso o usuário deverá realizar a busca de reserva pelo CPF.
    ▪ Caso exista mais de uma reserva no CPF da pessoa, o usuário deverá
    escolher qual reserva ele quer dar check – in.
    o O processo de check in é um processo automático, sendo necessário apenas
    alterar o STATUS da reserva de (R – Reservado) para (A – Ativo).
    o O sistema deverá apresentar mensagem de realização de check – in, ex: ‘Check
    in Realizado com sucesso !!!! ’.

● Saída do cliente (Check out).

    o Nessa tela o usuário terá a opção de dar a saída de um cliente no hotel, ou
    seja, realizar o check out.
    o Para isso o usuário deverá realizar a busca de reserva pelo CPF.
    o Caso exista mais de uma reserva no CPF da pessoa, o usuário deverá escolher
    qual reserva ele quer dar check – out.
    o O processo de check out é um processo automático, sendo necessário apenas
    alterar o STATUS da reserva de (A – Ativo) para (F - Finalizado)
    o O sistema deverá apresentar mensagem de realização de check – out, ex:
    ‘Check out Realizado com sucesso !!!! ’.

● Alteração de reserva

Para isso o usuário deverá realizar a busca de reserva pelo CPF.
Caso exista mais de uma reserva no CPF da pessoa, o usuário deverá escolher
qual reserva ele quer alterar.

O sistema deverá permitir a alteração dos seguintes campos:

    ▪ Número de pessoas
    ▪ Tipo do Quarto ( S – Standar, D – Deluxe, P – Premium)
    ▪ Número de dias
    ▪ Valor (Já que é calculado de forma automática)
    ▪ Status (R - Reservado, C – Cancelado, A – Ativo, F - Finalizado)

Ao inserir os novos dados sobre a reserva, o sistema deverá apresentar uma
mensagem de confirmação de alteração.

● Relatório de Reservas

Nessa tela, o sistema deverá apresentar as seguintes opções:

    ▪ 1 - Relatório de todas as reservas com status R.
    ▪ 2 - Relatório de todas as reservas com status C.
    ▪ 3 - Relatório de todas as reservas com status A.
    ▪ 4 - Relatório de todas as reservas com status F.
    ▪ 5 - Relatório total recebido (somar valor de todas as reservas
    finalizadas)
    ▪ 6 – Relatório de Reserva por pessoa (Pesquisa por CPF)