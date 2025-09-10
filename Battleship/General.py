"""
Objective: Create a grid from 0 to 'size' with '~' in each cell
Input: size represents the number of rows and columns the user wants for their grid
Output: board is the initialized grid to start the game
"""
def initialize_board(size):
    board = [['~' for _ in range(size + 1)] for _ in range(size + 1)]
    for i in range(1, size + 1):
        board[0][i] = i - 1
        board[i][0] = i - 1
    return board


"""
Objective: Display the board on the console so the user can see their ships
           and their previous shots to know where to shoot
Input: board is the initialized grid to start the game
Output: prints the board nicely formatted
"""
def show_board(board):
    for row in board:
        print(' '.join(map(str, row)))
    print()


"""
Objective: Verify that the player (user or computer) can
           place their ships at the chosen coordinates
Inputs: - board is the initialized grid to start the game
        - fleet_size is the composition chosen by the user for their fleet and the computer's fleet
        - ship is the ship for which we want to check if coordinates are valid
        - (x, y) are the cell coordinates to check
        - direction is the horizontal or vertical orientation chosen for placing the ship
Output: Boolean indicating whether the position is valid
"""
def check_position(board, fleet_size, ship, x, y, direction):
    ship_length = fleet_size[ship]

    if direction == 0:
        if y + 1 + ship_length > len(board):
            print()
            return False

        for i in range(ship_length):
            if board[x + 1][y + 1 + i] != '~':
                print()
                return False
            if x + 1 > 1 and board[x + 1 - 1][y + 1 + i] != '~':
                print()
                return False
            if x + 1 < len(board) - 1 and board[x + 1 + 1][y + 1 + i] != '~':
                print()
                return False
        if y + 1 > 1 and board[x + 1][y + 1 - 1] != '~':
            print()
            return False
        if y + 1 + ship_length < len(board) - 1 and board[x + 1][y + 1 + ship_length] != '~':
            print()
            return False

    elif direction == 1:
        if x + 1 - ship_length + 1 < 1:
            print()
            return False

        for i in range(ship_length):
            if board[x + 1 - i][y + 1] != '~':
                print()
                return False
            if y + 1 > 1 and board[x + 1 - i][y + 1 - 1] != '~':
                print()
                return False
            if y + 1 < len(board) - 1 and board[x + 1 - i][y + 1 + 1] != '~':
                print()
                return False
        if x + 1 - ship_length >= 1 and board[x + 1 - ship_length][y + 1] != '~':
            print()
            return False
        if x + 1 < len(board) - 1 and board[x + 1 + 1][y + 1] != '~':
            print()
            return False

    print()
    return True


"""
Objective: Display the user's board with their ships as they add them
Inputs: - board is the initialized grid to start the game
        - fleet_size is the composition chosen by the user for their fleet and the computer's fleet
        - ship is the ship for which we want to place coordinates
        - (x, y) are the cell coordinates to update
        - direction is the horizontal or vertical orientation chosen for placing the ship
Output: board updated with the player's ships
"""
def update_board(board, fleet_size, ship, x, y, direction):
    ship_length = fleet_size[ship]
    print()
    if direction == 0:
        print()
        for i in range(ship_length):
            board[x + 1][y + 1 + i] = ship[0]
    elif direction == 1:
        for i in range(ship_length):
            board[x + 1 - i][y + 1] = ship[0]
    return board


"""
Objective: Register the positions of the player's ships (user and computer) to track game progress
Inputs: - ship_locations is a dictionary mapping 'ships' to 'fleet_count'
        - ship is the ship for which coordinates are being registered
        - (x, y) are the cell coordinates
        - direction is the horizontal or vertical orientation of the ship
Output: ship_locations updated with the newly placed ship
"""
def register_positions(ship_locations, ship, x, y, direction, ship_length):
    positions = []
    if direction == 0:  # Horizontal
        for i in range(ship_length):
            positions.append((x, y + i))
    elif direction == 1:  # Vertical
        for i in range(ship_length):
            positions.append((x - i, y))
    if ship in ship_locations:
        ship_locations[ship] += [positions]
    else:
        ship_locations[ship] = positions


"""
Objective: Test function to verify that ships are properly placed
Inputs: ship_locations is the dictionary of all player's ships (user or computer)
Output: prints the type of ships with their coordinates (e.g., submarine (1, 2))
"""
def show_results(ship_locations):
    print("Ship locations:")
    for ship, positions in ship_locations.items():
        print(f"{ship}: {positions}")


"""
Objective: Check if all of a player's ships have been sunk by the other player
Inputs: - board is the grid with the player's ships
        - ship_letters is a list of the first letters of each ship type
Output: Boolean indicating if the board has no ships left (game over)
"""
def test_game_over(board, ship_letters):
    return all(cell not in ship_letters for row in board for cell in row)


"""
Objective: Check if a ship is hit after a shot
Inputs: - board is the grid with the player's ships
        - (x, y) are the cell coordinates of the shot
Output: Boolean indicating if the position is a hit
"""
def check_ship_hit(board, x, y):
    if board[x + 1][y + 1] == 'X':
        return True


"""
Objective: Determine if a ship has been sunk after a shot
Inputs: - board is the initialized grid
        - (x, y) is the pair of coordinates shot in the last turn
        - computer_ship_locations is the dictionary of all computer ships
        - first_letters are the keys corresponding to each ship type
Output: Boolean indicating if the ship has been completely sunk
"""
def check_ship_sunk(board, x, y, computer_ship_locations, first_letters):
    for ship, positions_list in computer_ship_locations.items():
        for k in range(len(positions_list)):
            for positions in positions_list[k]:
                if (x, y) == positions:
                    sunk = True
                    for pos_x, pos_y in positions_list[k]:
                        if board[pos_x + 1][pos_y + 1] in first_letters:
                            sunk = False
                            break
                    if sunk:
                        return True, positions_list[k]
    return False, None


"""
Objective: Mark a ship as sunk after a shot
Inputs: - board is the initialized grid
        - result_board is the board tracking previous shots
        - positions_list are the coordinates of the computer's ship
Output: Marks 'O' on both the main board and the result board
"""
def mark_ship_sunk(board, result_board, positions_list):
    for x, y in positions_list:
        board[x + 1][y + 1] = 'O'
        result_board[x + 1][y + 1] = 'O'
