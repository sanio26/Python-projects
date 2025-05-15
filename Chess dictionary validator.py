print("Sanio Frederic,1AY24AI099,SEC-O")
def is_valid_chess_board(board):
    valid_positions = [f"{row}{col}" for row in range(1, 9) for col in 'abcdefgh']
    piece_types = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']

    piece_counts = {
        'w': {'total': 0, 'pawn': 0, 'king': 0},
        'b': {'total': 0, 'pawn': 0, 'king': 0}
    }

    for position, piece in board.items():
        # Check position
        if position not in valid_positions:
            print(f"Invalid position: {position}")
            return False

        # Check piece name
        if len(piece) < 2 or piece[0] not in ('w', 'b') or piece[1:] not in piece_types:
            print(f"Invalid piece: {piece}")
            return False

        color = piece[0]
        p_type = piece[1:]

        piece_counts[color]['total'] += 1
        if p_type == 'pawn':
            piece_counts[color]['pawn'] += 1
        if p_type == 'king':
            piece_counts[color]['king'] += 1

    # Rule checks
    for color in ('w', 'b'):
        if piece_counts[color]['king'] != 1:
            print(f"Invalid number of {color} kings: {piece_counts[color]['king']}")
            return False
        if piece_counts[color]['pawn'] > 8:
            print(f"Too many {color} pawns: {piece_counts[color]['pawn']}")
            return False
        if piece_counts[color]['total'] > 16:
            print(f"Too many {color} pieces: {piece_counts[color]['total']}")
            return False

    return True

# Example usage
chess_board = {
    '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
    '5h': 'bqueen', '3e': 'wking', '7d': 'wpawn'
}

if __name__ == "__main__":
    if is_valid_chess_board(chess_board):
        print("Chess board is valid.")
    else:
        print("Chess board is invalid.")
