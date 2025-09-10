from general import show_board, check_ship_sunk, mark_ship_sunk

"""
Purpose: Make a shot as the user
Inputs: - board initialized
        - computer_ship_locations dictionary of all computer ships
        - first_letters list of initials of ship types
Outputs: - sunk_ships total sunk by the user this turn
         - hit_ships total hit by the user this turn
         - board updated
         - (x, y) coordinates of the user’s shot
"""
def user_shot(board, computer_ship_locations, first_letters):
    n = len(board)
    temp_board = [[board[x][y] for y in range(n)] for x in range(n)]
    for x in range(1, n):
        for y in range(1, n):
            if board[x][y] in ('.', 'X', 'O'):
                temp_board[x][y] = board[x][y]
            else:
                temp_board[x][y] = '~'
    
    show_board(temp_board)
    print("It's your turn!")
    
    while True:
        try:
            x = int(input(f"Enter the x coordinate (between 0 and {n - 2}): "))
            y = int(input(f"Enter the y coordinate (between 0 and {n - 2}): "))
            if 0 <= x < n - 1 and 0 <= y < n - 1:
                break
            else:
                print("Coordinates out3 of range. Try again.")
        except ValueError:
            print("Invalid input. Try again.")
    
    sunk_ships = 0
    hit_ships = 0
    
    if board[x + 1][y + 1] == '~':
        print("\nMissed, it was water!\n")
        board[x + 1][y + 1] = '.'
        temp_board[x + 1][y + 1] = '.'
    else:
        print(f"\nGreat, you hit at ({x}, {y})!\n")
        board[x + 1][y + 1] = 'X'
        temp_board[x + 1][y + 1] = 'X'
        hit_ships += 1

        ship_sunk, positions = check_ship_sunk(board, x, y, computer_ship_locations, first_letters)

        if ship_sunk:
            print("\nAmazing, you sunk a ship!\n")
            mark_ship_sunk(board, temp_board, positions)
            sunk_ships += 1

    show_board(temp_board)
    
    return sunk_ships, hit_ships, board, x, y
