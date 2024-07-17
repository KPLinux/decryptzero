import chess, chess.svg
import copy


def find_valid_move_lists_helper(starting_fen, starting_move, move_list):
    i = 0
    valid_move_lists = []
    board = chess.Board(starting_fen)
    while i in range(starting_move, len(move_list)): # Iterate through all moves in the game
        if move_list[i] is None: # Case 1: Current move was marked missing
            chess.svg.board(board)
            legal_moves = board.legal_moves
            for j in legal_moves:
                current_list = copy.deepcopy(move_list)
                current_list[i] = board.san(j)
                valid_move_lists += find_valid_move_lists_helper(board.fen(), i, current_list)
            return valid_move_lists
        else: # Current move
            try:
                board.push_san(move_list[i]) # Case 2: Current move is valid
            except Exception:
                move_list[i] = None 
                i -= 1 # Case 3: Current move is invalid
        i += 1
    current_list = copy.deepcopy(move_list)
    return [current_list] # Case 4: Reached end of move list

def find_valid_move_lists(move_list):
    starting_fen = chess.Board().fen()
    return find_valid_move_lists_helper(starting_fen, 0, move_list)

print(find_valid_move_lists(['e4', 'e5', 'Nf3', None, 'Bc4', 'Nf6', 'Ng5', 'd5', 'exd5', 'Na5']))