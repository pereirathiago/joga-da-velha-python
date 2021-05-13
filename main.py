from jogo import *

c = ""
while c != "N":
    player = 0
    board = criarBoard()
    winner = verificaGanhador(board)
    while(not winner):
        printBoard(board)
        print("===================")
        i = getInputValido("Digite a linha: ")
        j = getInputValido("Digite a coluna: ")
        
        if(verificaMovimento(board, i, j)):
            fazMovimento(board, i, j, player)
            player = (player + 1)%2
        else:
            print("Cê não ta vendo q ja tem ali")
        
        winner = verificaGanhador(board)

    print("===================")
    printBoard(board)
    print("Ganhador = ", winner)
    print("===================")

    c = input('Jogar novamente[S/N]: ')