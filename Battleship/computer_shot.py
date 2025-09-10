import random
from general import check_ship_sunk, mark_ship_sunk

def generate_random_coordinate(size: int) -> tuple[int, int]:
    """
    Generates random coordinates for a shot.

    Returns
    -------
    tuple
        Randomly chosen coordinates (x, y) within the grid.
    """
    return random.randint(0, size - 1), random.randint(0, size - 1)

def mark_nearby_sunk_areas(x: int, y: int, positions: list, cells_to_avoid: set):
    """
    Marks cells around a sunk ship to avoid in future shots.
    """
    if len(positions) == 1:
        cells_to_avoid.update({(x+1, y), (x-1, y), (x, y+1), (x, y-1)})
    else:
        if positions[0][0] != positions[1][0]:
            cells_to_avoid.update({(positions[0][0]+1, y), (positions[-1][0]-1, y)})
            for k in range(len(positions)):
                cells_to_avoid.update({(positions[k][0], y-1), (positions[k][0], y+1)})
        else:
            cells_to_avoid.update({(x, positions[0][1]-1), (x, positions[-1][1]+1)})
            for k in range(len(positions)):
                cells_to_avoid.update({(x-1, positions[k][1]), (x+1, positions[k][1])})

def update_probabilities(probabilities: list, shot_x: int, shot_y: int, size: int):
    """
    Adds neighboring cells of a hit to the list of probable targets.
    """
    new_coords = [(shot_x + 1, shot_y), (shot_x - 1, shot_y), (shot_x, shot_y + 1), (shot_x, shot_y - 1)]
    probabilities.extend([coord for coord in new_coords if 0 <= coord[0] < size and 0 <= coord[1] < size])

def remove_associated_probabilities(probabilities: list, positions: list):
    """
    Removes cells associated with a sunk ship from probabilities.
    """
    for pos in positions:
        if pos in probabilities:
            probabilities.remove(pos)

def prioritize_direction(probabilities: list, shot_x: int, shot_y: int, direction: str, size: int):
    """
    Focuses next probable shots along the detected ship direction.
    """
    if direction == "horizontal":
        probabilities.extend([(shot_x, shot_y - 1), (shot_x, shot_y + 1)])
    elif direction == "vertical":
        probabilities.extend([(shot_x - 1, shot_y), (shot_x + 1, shot_y)])
    probabilities[:] = [coord for coord in probabilities if 0 <= coord[0] < size and 0 <= coord[1] < size]

def strategic_computer_shot(
    board: list, size: int, fleet_size: dict, ship_locations: dict,
    previous_shots: set, cells_to_avoid: set, first_letters: list,
    probabilities: list, hits: list
):
    """
    Makes a strategic shot based on probabilities and previous hits.

    Returns
    -------
    sunk_ships
        Number of ships sunk this turn.
    hit_ships
        Number of ships hit this turn.
    board
        Updated board.
    x, y
        Coordinates of the shot.
    """
    sunk_ships = 0
    hit_ships = 0
    if probabilities:
        x, y = probabilities.pop(0)
    else:
        x, y = generate_random_coordinate(size)
        
    while (x, y) in previous_shots or (x, y) in cells_to_avoid:
        if probabilities:
            x, y = probabilities.pop(0)
        else:
            x, y = generate_random_coordinate(size)
            
    previous_shots.add((x, y))
    
    if board[x + 1][y + 1] in first_letters:
        print(f"Hit at ({x}, {y})!")
        board[x + 1][y + 1] = 'X'
        hits.append((x, y))
        ship_sunk, positions = check_ship_sunk(board, x, y, ship_locations, first_letters)
        hit_ships += 1
        if ship_sunk:
            print("Sunk!")
            sunk_ships += 1
            mark_ship_sunk(board, board, positions)
            mark_nearby_sunk_areas(x, y, positions, cells_to_avoid)
            remove_associated_probabilities(probabilities, positions)
            hits.clear()
        else:
            if len(hits) > 1:
                direction = "horizontal" if hits[-1][0] == hits[-2][0] else "vertical"
                prioritize_direction(probabilities, x, y, direction, size)
            else:
                update_probabilities(probabilities, x, y, size)
    else:
        print(f"Miss at ({x}, {y})!")
        board[x + 1][y + 1] = '.'

    return sunk_ships, hit_ships, board, x, y

def random_computer_shot(
    board: list, size: int, fleet_size: dict, ship_locations: dict,
    previous_shots: set, first_letters: list
):
    """
    Makes a random shot on the board.

    Returns
    -------
    sunk_ships
        Number of ships sunk this turn.
    hit_ships
        Number of ships hit this turn.
    board
        Updated board.
    x, y
        Coordinates of the shot.
    """
    shot_successful = False
    sunk_ships = 0
    hit_ships = 0
    
    while not shot_successful:
        x, y = generate_random_coordinate(size)
        if (x, y) not in previous_shots:
            shot_successful = True
            previous_shots.add((x, y))
            if board[x + 1][y + 1] in first_letters:
                print(f"Hit at ({x}, {y})!")
                board[x + 1][y + 1] = 'X'
                ship_sunk, positions = check_ship_sunk(board, x, y, ship_locations, first_letters)
                if ship_sunk:
                    print("Sunk!")
                    mark_ship_sunk(board, board, positions)
                    sunk_ships += 1
                else:
                    hit_ships += 1
            else:
                print(f"Miss at ({x}, {y})!")
                board[x + 1][y + 1] = '.'

    return sunk_ships, hit_ships, board, x, y
