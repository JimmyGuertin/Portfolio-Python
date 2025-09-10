from general import show_board, check_position, update_board, register_positions

"""
Purpose: Ensure that the user's input is an integer when choosing game parameters
Input: message string displayed to the user
Output: value entered by the user (or prints an error message to retry)
"""
def get_integer(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Please enter a valid integer.")

"""
Purpose: Ask the user where they want to place each ship in their fleet
Inputs: - board initialized
        - fleet_size dictionary with the size of each type of ship
        - fleet_count dictionary with the number of each type of ship in the user's fleet
Output: ship_locations dictionary representing the user's ships with their positions
"""
def place_ships(board, fleet_size, fleet_count):
    ship_locations = {ship: [] for ship in fleet_count}

    for ship in fleet_count.keys():
        for num in range(fleet_count[ship]):
            placed = False
            while not placed:
                print(f"Place {ship} number {num + 1}:")
                show_board(board)
                n = len(board)

                x = get_integer(f"Enter the row coordinate for the origin (0-{n-1}): ")
                y = get_integer(f"Enter the column coordinate for the origin (0-{n-1}): ")

                if x < 0 or x >= len(board) or y < 0 or y >= len(board):
                    print(f"Invalid values. Coordinates must be between 0 and {n-1}. Please try again.\n")
                    continue

                direction = 0  
                if ship != 'Lanchas':  # Small boat always horizontal
                    direction = get_integer("Direction horizontal (right) (0) / vertical (up) (1): ")

                    if direction not in [0, 1]:
                        print("Invalid direction. Must be 0 (horizontal) or 1 (vertical). Please try again.\n")
                        continue

                if check_position(board, fleet_size, ship, x, y, direction):
                    board = update_board(board, fleet_size, ship, x, y, direction)
                    register_positions(ship_locations, ship, x, y, direction, fleet_size[ship])
                    placed = True
                else:
                    print("No space available for the ship.\n")
    
    return ship_locations
