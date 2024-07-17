import chess

board = chess.Board()

test_game = ['e4', 'e5', 'Qf3', 'Nc6', 'Bc5', 'Qxf7#']

i = 0

# iterates through each move in the game
for ply in test_game:
    
    # makes the move
    board.push_san(ply)
    
    # creates a list of all legal moves for the next player to move in that position
    legal_moves_list = [board.san(move) for move in board.legal_moves]
    print(legal_moves_list)

    '''
    checks if the index is greater than the length of the game
    useful for terminating the process at the end of the game
    '''
    if i > len(test_game):
        break

    # checks if the next notated move is illegal
    elif test_game[i + 1] not in legal_moves_list:
        for lm in legal_moves_list:
            board.push_san(lm)
            legal_moves_list2 = [board.san(move) for move in board.legal_moves]
            if test_game[i + 1] in legal_moves_list2:
                test_game.insert(i + 1, lm) 
            board.pop()
    i += 1

    # checks if the current move is unknown
    if ply == None:
        i += 1
        continue

print(test_game)