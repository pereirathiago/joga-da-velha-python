from jogo import *

from minimax import movimentoIA

c = "S"
jogador = 0 # jogador 1
while c == "S":
    board = criarBoard()
    ganhador = verificaGanhador(board)
    while(not ganhador):
        printBoard(board)
        print("===================")
        if(jogador == 0):
            i,j = movimentoIA(board, jogador)
            # i = getInputValido("Digite a linha: ")
            # j = getInputValido("Digite a coluna: ")
        else:
            i,j = movimentoIA(board, jogador)
            # i = getInputValido("Digite a linha: ")
            # j = getInputValido("Digite a coluna: ")
        
        if(verificaMovimento(board, i, j)):
            fazMovimento(board, i, j, jogador)
            jogador = (jogador + 1)%2
        else:
            print("Cê não ta vendo q ja tem ali")
        
        ganhador = verificaGanhador(board)

    print("===================")
    printBoard(board)
    print(f"Ganhador = {ganhador}")
    print("===================")

    c = input("Quer jogar mais [S/N]: ")
