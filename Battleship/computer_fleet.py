import random
from general import show_board, check_position, update_board, register_positions

def generate_random_coordinates(size: int, ship: str, direction: int, fleet_size: dict) -> tuple[int, int]:
    """
    Generates random coordinates to place a ship.
    
    Returns coordinates that fit the grid based on ship size and direction.
    """
    ship_size = fleet_size[ship]
    if direction == 0:  # horizontal
        x = random.randint(0, size - ship_size)
        y = random.randint(0, size - 1)
    else:  # vertical
        x = random.randint(1, size - 1)
        y = random.randint(0, size - ship_size)
    return x, y

def generate_random_direction() -> int:
    """
    Generates a random direction: 0 = horizontal, 1 = vertical.
    """
    return random.randint(0, 1)

def place_random_ships(board: list[list[str]], fleet_size: dict, fleet_count: dict, size: int) -> dict:
    """
    Places all ships of the computer fleet randomly on the board.
    
    Returns a dictionary with ship locations.
    """
    ship_locations = {ship: [] for ship in fleet_count}

    for ship in fleet_count.keys():
        for _ in range(fleet_count[ship]):
            success = False
            while not success:
                direction = generate_random_direction() if ship != 'Lanchas' else 0
                x, y = generate_random_coordinates(size, ship, direction, fleet_size)

                if check_position(board, fleet_size, ship, x, y, direction):
                    board = update_board(board, fleet_size, ship, x, y, direction)
                    register_positions(ship_locations, ship, x, y, direction, fleet_size[ship])
                    success = True
                    # show_board(board)  # Optional: verify ship placement
    return ship_locations
