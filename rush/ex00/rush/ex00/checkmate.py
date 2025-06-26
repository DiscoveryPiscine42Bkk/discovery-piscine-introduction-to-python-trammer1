def checkmate(board_str):
    
    board = [list(row) for row in board_str.strip().split('\n')]
    size = len(board)

    def in_bounds(x, y):
        return 0 <= x < size and 0 <= y < size

    # หาตำแหน่งของ King 'K'
    king_pos = None
    for y in range(size):
        for x in range(size):
            if board[y][x] == 'K':
                king_pos = (x, y)
                break
        if king_pos:
            break
    if not king_pos:
        print("Fail")
        return
    kx, ky = king_pos

    # Pawn
    pawn_dirs = [(-1, 1), (1, 1)]
    for dx, dy in pawn_dirs:
        x, y = kx + dx, ky + dy
        if in_bounds(x, y) and board[y][x] == 'P':
            print("Success")
            return

    # Bishop / Queen 
    for dx, dy in [(-1, -1), (1, -1), (1, 1), (-1, 1)]:
        x, y = kx + dx, ky + dy
        while in_bounds(x, y):
            piece = board[y][x]
            if piece == '.':
                x += dx; y += dy
                continue
            if piece in ('B', 'Q'):
                print("Success")
                return
            break

    #  Rook / Queen 
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = kx + dx, ky + dy
        while in_bounds(x, y):
            piece = board[y][x]
            if piece == '.':
                x += dx; y += dy
                continue
            if piece in ('R', 'Q'):
                print("Success")
                return
            break

   
    print("Fail")
