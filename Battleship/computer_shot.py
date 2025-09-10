import random
from general import check_ship_sunk, mark_ship_sunk

"""
Purpose: Generate random coordinates for a shot
Input: size is the dimension of the grid
Output: x, y are randomly chosen coordinates
"""
def generate_random_coordinate(size):
    return random.randint(0, size - 1), random.randint(0, size - 1)


"""
Purpose: Used in strategic computer shots because two ships cannot touch
Inputs: - (x, y) coordinates of the last shot that hit a ship
        - positions are the locations of ships on the grid
        - cells_to_avoid is the set of cells to avoid for next shots (water or sunk ships)
Output: Updates cells_to_avoid set
"""
def mark_nearby_sunk_areas(x, y, positions, cells_to_avoid):
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


"""
Purpose: Track most probable cells for the computer to target
Inputs: - probabilities list of most likely ship locations
        - shot_x, shot_y last successful shot coordinates
        - size of the grid
Output: updates probabilities list
"""
def update_probabilities(probabilities, shot_x, shot_y, size):
    new_coords = [(shot_x + 1, shot_y), (shot_x - 1, shot_y), (shot_x, shot_y + 1), (shot_x, shot_y - 1)]
    probabilities.extend([coord for coord in new_coords if 0 <= coord[0] < size and 0 <= coord[1] < size])


"""
Purpose: Remove probable cells associated with a ship that has just been sunk
Inputs: - probabilities list of likely ship locations
        - positions of the sunk ship
Output: probabilities list updated
"""
def remove_associated_probabilities(probabilities, positions):
    for pos in positions:
        if pos in probabilities:
            probabilities.remove(pos)


"""
Purpose: Prioritize direction after hitting a ship
Inputs: - probabilities list of likely ship locations
        - shot_x, shot_y last shot coordinates
        - direction "horizontal" or "vertical"
        - size of the grid
Output: updates probabilities list
"""
def prioritize_direction(probabilities, shot_x, shot_y, direction, size):
    if direction == "horizontal":
        probabilities.extend([(shot_x, shot_y - 1), (shot_x, shot_y + 1)])
    elif direction == "vertical":
        probabilities.extend([(shot_x - 1, shot_y), (shot_x + 1, shot_y)])
    probabilities[:] = [coord for coord in probabilities if 0 <= coord[0] < size and 0 <= coord[1] < size]


"""
Purpose: Make a strategic computer shot using probability logic
Inputs: - board initialized
        - size of the game grid
        - fleet_size dictionary of ship types to lengths
        - ship_locations dictionary of user ship coordinates
        - previous_shots set to avoid repeated shots
        - cells_to_avoid set
        - first_letters list of ship initials
        - probabilities list
        - hits list of cells hit but not sunk
Outputs: - sunk_ships total sunk by computer this turn
         - hit_ships total hit by computer this turn
         - board updated
         - (x, y) shot coordinates
"""
def strategic_computer_shot(board, size, fleet_size, ship_locations, previous_shots, cells_to_avoid, first_letters, probabilities, hits):
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
            mark_ship_sunk(board, board,positions)
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


"""
Purpose: Make a random computer shot
Inputs: - board initialized
        - size of the game grid
        - fleet_size dictionary of ship types to lengths
        - ship_locations dictionary of user ship coordinates
        - previous_shots set to avoid repeated shots
        - first_letters list of ship initials
Outputs: - sunk_ships total sunk by computer this turn
         - hit_ships total hit by computer this turn
         - board updated
         - (x, y) shot coordinates
"""
def random_computer_shot(board, size, fleet_size, ship_locations, previous_shots, first_letters):
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
