from jogo import *

from minimax import movimentoIA

c = ""
while c != "N":
    player = 0
    board = criarBoard()
    ganhador = verificaGanhador(board)
    while(not ganhador):
        printBoard(board)
        print("===================")

        if(player == 0):
            i,j = movimentoIA(board, player)
        else:
            i,j = movimentoIA(board, player)
            # i = getInputValido("Digite a linha: ")
            # j = getInputValido("Digite a coluna: ")
        
        if(verificaMovimento(board, i, j)):
            fazMovimento(board, i, j, player)
            player = (player + 1)%2
        else:
            print("Cê não ta vendo q ja tem ali")
        
        ganhador = verificaGanhador(board)

    print("===================")
    printBoard(board)
    print(f"Ganhador = {player}")
    print("===================")

    c = input('Jogar novamente[S/N]: ')