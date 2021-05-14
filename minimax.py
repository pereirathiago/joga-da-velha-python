from jogo import vazio, token, verificaGanhador

def movimentoIA(board, player):
    possibilidades = getPosicoes(board)
    bestValue = None
    bestMove = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[player]
        valor = minimax(board, player)
        board[possibilidade[0]][possibilidade[1]] = vazio
        if(bestValue is None):
            bestValue = valor
            bestMove = possibilidade
        elif(player == 0):
            if(valor > bestValue):
                bestValue = valor
                bestMove = possibilidade
        elif(player == 1):
            if(valor < bestValue):
                bestValue = valor
                bestMove = possibilidade

    return bestMove[0], bestMove[1]

def getPosicoes(board):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] == vazio):
                posicoes.append([i, j])
    
    return posicoes

score = {
    "EMPATE": 0,
    "X": 1,
    "O": -1
}

def minimax(board, player):
    ganhador = verificaGanhador(board)
    if(ganhador):
        return score[ganhador]
    player = (player + 1)%2
    
    possibilidades = getPosicoes(board)
    bestValue = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[player]
        valor = minimax(board, player)
        board[possibilidade[0]][possibilidade[1]] = vazio

        if(bestValue is None):
            bestValue = valor
        elif(player == 0):
            if(valor > bestValue):
                bestValue = valor
        elif(player == 1):
            if(valor < bestValue):
                bestValue = valor

    return bestValue