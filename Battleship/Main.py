from rules import define_fleet, define_options, define_size, define_mode, define_computer_level
from general import initialize_board, show_results, show_board, test_game_over, check_ship_hit
from user_fleet import place_ships, get_integer
from computer_fleet import place_random_ships
from computer_shot import strategic_computer_shot, random_computer_shot, check_ship_sunk
from user_shot import user_shot
from game import Play

def main():
    print()
    welcome_message = "Welcome to Battleship!\n"
    print(welcome_message.center(60))

    print("=> To start, choose the size of the grid you will play on.")
    size = define_size()

    print()
    print("\n=> Now you will choose the ships that will make up your fleet and your opponent's fleet. Be careful, this choice can be strategic...\n")
    option = define_options(size)

    fleet_count = define_fleet(size, option)
    fleet_size = {'Aircraft Carrier': 5, 'Battleships': 4, 'Submarines': 3, 'Cruisers': 2, 'Boats': 1}
    first_letters = [key[0] for key in fleet_size.keys()]
    user_board = initialize_board(size)
    computer_board = initialize_board(size)

    print()
    print("=> Now place your ships on the grid.\n")
    user_ship_locations = place_ships(user_board, fleet_size, fleet_count)
    computer_ship_locations = place_random_ships(computer_board, fleet_size, fleet_count, size)
    print()
    
    # Three lines for testing above functionality. You can comment them out
    # show_results(user_ship_locations) 
    # show_results(computer_ship_locations)
    # show_board(computer_board)

    previous_shots = set()
    cells_to_avoid = set()
    probable_shots = []
    hit = []

    # Tests to verify individual shot functions
    """ USER
    user_shot(computer_board, computer_ship_locations, first_letters)  
    """

    """ STRATEGIC COMPUTER
    strategic_computer_shot(user_board, size, fleet_size, user_ship_locations, previous_shots, cells_to_avoid, first_letters, probable_shots, hit)
    """

    """ RANDOM COMPUTER
    random_computer_shot(user_board, size, fleet_size, user_ship_locations, previous_shots, first_letters)
    """

    level = define_computer_level()
    mode = define_mode()
    
    Play(computer_board, computer_ship_locations, first_letters, user_board, size, fleet_size, user_ship_locations, previous_shots, mode, level, cells_to_avoid, probable_shots, hit)
        
if __name__ == "__main__":
    main()
