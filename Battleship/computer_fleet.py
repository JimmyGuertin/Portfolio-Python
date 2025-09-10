import random
from general import show_board, check_position, update_board, register_positions

"""
Objective: Generate random coordinates to place the computer's ships later
Input: - size is the dimension of the grid
       - ship is the ship to place
       - direction is the random direction
       - fleet_size is the composition chosen by the user for their fleet and the computer's fleet
Output: (x, y) the pair of coordinates randomly chosen to place the ship
"""
def generate_random_coordinates(size, ship, direction, fleet_size):
    ship_size = fleet_size[ship]
    if direction == 0:
        x = random.randint(0, size - ship_size)
        y = random.randint(0, size - 1)
    else:
        x = random.randint(1, size - 1)
        y = random.randint(0, size - ship_size)
    return x, y


"""
Objective: Generate random direction to place the computer's ships later
Input: None
Output: 0 or 1 randomly
"""
def generate_random_direction():
    return random.randint(0, 1)


"""
Objective: Place each ship of the computer's fleet
Input: - initialized board
       - fleet_size is the composition chosen by the user for their fleet and the computer's fleet
       - fleet_count is the number of each type of ship in the user's fleet
       - size is the dimension of the grid
Output: ship_locations containing all the computer's ships
"""
def place_random_ships(board, fleet_size, fleet_count, size):
    ship_locations = {ship: [] for ship in fleet_count}

    for ship in fleet_count.keys():
        for num in range(fleet_count[ship]):
            success = False
            while not success:
                direction = generate_random_direction() if ship != 'Lanchas' else 0
                x, y = generate_random_coordinates(size, ship, direction, fleet_size)

                if check_position(board, fleet_size, ship, x, y, direction):
                    board = update_board(board, fleet_size, ship, x, y, direction)
                    register_positions(ship_locations, ship, x, y, direction, fleet_size[ship])
                    success = True
                    # show_board(board) # to verify if ships are placed correctly
    return ship_locations
