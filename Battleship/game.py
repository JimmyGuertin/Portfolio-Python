from general import test_game_over, check_ship_hit, show_board
from user_fleet import get_integer
from computer_shot import strategic_computer_shot, random_computer_shot
from user_shot import user_shot

"""
Objective: Run the game using two different modes so players can play together
Inputs: - computer_board refers to the computer's ships on the grid
        - computer_ship_locations represents the computer fleet (coordinates as pairs)
        - first_letters represent the first letter of each ship type
        - user_board refers to the user's ships on the grid
        - size, option chosen by the user in Main: dimension of the game grid
        - fleet_size, dictionary mapping ship types to their size in cells
        - user_ship_locations represents the user's fleet (coordinates as pairs)
        - previous_shots represents previous computer shots in strategic mode
        - mode, option chosen by the user in Main: gameplay mode (alternating or continuous)
        - level, option chosen by the user in Main: computer shot type (strategic or random)
        - cells_to_avoid is the list used by the computer for strategic shooting
        - probable_shots is a list of cells with higher probability to contain a ship
        - hit represents cells hit in the computer's strategic shots
Output: None
"""
def Play(computer_board, computer_ship_locations, first_letters, user_board, size, fleet_size, user_ship_locations, previous_shots, mode, level, cells_to_avoid, probable_shots, hit):

    # alternating mode: players take turns until reaching a number of shots each player entered at game start
    if mode == 1:
        print()
        turn_count = get_integer("Enter the number of shots per player: ")
        total_user_ships_sunk = 0
        total_user_ships_hit = 0
        total_computer_ships_sunk = 0
        total_computer_ships_hit = 0

        for turn in range(1, turn_count + 1):
            RED = "\033[31m"
            RESET = "\033[0m"
            print(RED + f"\nTurn {turn}:\n" + RESET)
            
            ships_sunk_user, ships_hit_user, board, x, y = user_shot(computer_board, computer_ship_locations, first_letters)
            total_user_ships_sunk += ships_sunk_user
            total_user_ships_hit += ships_hit_user

            print ("_______________________________")
            print()
            print("It's the computer's turn!")
            if level == 1:
                ships_sunk_computer, ships_hit_computer, board, x, y = random_computer_shot(user_board, size, fleet_size, user_ship_locations, previous_shots, first_letters)
            else:
                ships_sunk_computer, ships_hit_computer, board, x, y = strategic_computer_shot(user_board, size, fleet_size, user_ship_locations, previous_shots, cells_to_avoid, first_letters, probable_shots, hit)
            total_computer_ships_sunk += ships_sunk_computer
            total_computer_ships_hit += ships_hit_computer
            
            print("\nYour grid with the computer's shots:")
            show_board(user_board)

            print ("_______________________________")
            print()

        print("\nFinal results:")
        print(f"Ships sunk by player: {total_user_ships_sunk}")
        print(f"Ships hit by player: {total_user_ships_hit}")
        print(f"Ships sunk by computer: {total_computer_ships_sunk}")
        print(f"Ships hit by computer: {total_computer_ships_hit}")

        if total_user_ships_sunk > total_computer_ships_sunk:
            print(f"\nCongratulations! You won. You sunk {total_user_ships_sunk} opponent ship(s) vs {total_computer_ships_sunk}.")
        elif total_user_ships_sunk < total_computer_ships_sunk:
            print(f"\nToo bad! The computer won. You sunk {total_user_ships_sunk} opponent ship(s) vs {total_computer_ships_sunk}.")
        elif total_user_ships_sunk == total_computer_ships_sunk and total_user_ships_hit > total_computer_ships_hit:
            print(f"\nCongratulations! You won. You hit {total_user_ships_hit} opponent ship(s) vs {total_computer_ships_hit}.")
        elif total_user_ships_sunk == total_computer_ships_sunk and total_user_ships_hit < total_computer_ships_hit:
            print(f"\nToo bad! The computer won. You hit {total_user_ships_hit} opponent ship(s) vs {total_computer_ships_hit}.")
        else:
            print(f"\nIt's a tie. Each sunk {total_user_ships_sunk} ship(s).")

    # continuous mode: players shoot as long as they hit opponent ships
    # if they hit water, it's the other player's turn
    # game ends when one player sinks the entire fleet of the opponent
    elif mode == 2:
        print()
        user_turn = True # user starts
        game_over = False # game continues while game_over = False
        total_user_ships_sunk = 0
        total_computer_ships_sunk = 0
        total_user_ships_hit = 0
        total_computer_ships_hit = 0
        
        while not game_over:
            if user_turn: # user plays
                print ("_______________________________")
                print()
                print("\nPlayer's turn:\n")
                ships_sunk_user, ships_hit_user, user_shot_board, x, y = user_shot(computer_board, computer_ship_locations, first_letters)
                total_user_ships_sunk += ships_sunk_user
                total_user_ships_hit += ships_hit_user
                
                if test_game_over(computer_board, first_letters):
                    print("\nCongratulations! You won. You sank all opponent ships.")
                    game_over = True

                elif check_ship_hit(user_shot_board, x, y):
                    user_turn = True
                
                else:
                    user_turn = False
            
            else:
                print ("_______________________________")
                print()
                print("\nComputer's turn:\n")
                if level == 1:
                    ships_sunk_computer, ships_hit_computer, computer_shot_board, x, y = random_computer_shot(user_board, size, fleet_size, user_ship_locations, previous_shots, first_letters)
                else:
                    ships_sunk_computer, ships_hit_computer, computer_shot_board, x, y = strategic_computer_shot(user_board, size, fleet_size, user_ship_locations, previous_shots, cells_to_avoid, first_letters, probable_shots, hit)
                print()
                print("Your grid with the computer's shots:")
                show_board(user_board)

                total_computer_ships_sunk += ships_sunk_computer
                total_computer_ships_hit += ships_hit_computer
                
                if test_game_over(user_board, first_letters):
                    print("\nToo bad! The computer won. It sank all your ships.")
                    game_over = True

                elif check_ship_hit(computer_shot_board, x, y):
                    user_turn = False
                
                else:
                    user_turn = True
