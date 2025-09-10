from user_fleet import get_integer

def define_size():
    while True:
        size = get_integer('You can choose between 5 (5x5 grid) or 10 (10x10 grid): ')
        if size in (5, 10):
            return size
        else:
            print('Please enter a valid value (5 or 10).')

def define_options(size):
    if size == 5:
        option = get_integer('Option 1: 1 Battleship, 1 Submarine, 1 Boat\n'
                             'Option 2: 1 Submarine, 2 Cruisers\n'
                             'Option 3: 2 Cruisers, 2 Boats\n'
                             '\nSelect an option: ')
        while option not in (1, 2, 3):
            print('Please enter a valid option (1, 2, or 3).')
            option = get_integer('Option 1: 1 Battleship, 1 Submarine, 1 Boat\n'
                                 'Option 2: 1 Submarine, 2 Cruisers\n'
                                 'Option 3: 2 Cruisers, 2 Boats\n'
                                 '\nSelect an option: ')
        return option
    else:
        option = get_integer('Option 1: 1 Aircraft Carrier, 2 Battleships, 3 Submarines, 4 Cruisers\n'
                             'Option 2: 1 Aircraft Carrier, 1 Battleship, 2 Submarines, 3 Cruisers\n'
                             'Option 3: 1 Battleship, 2 Submarines, 3 Cruisers, 4 Boats\n'
                             '\nSelect an option: ')
        while option not in (1, 2, 3):
            print('Please enter a valid option (1, 2, or 3).')
            option = get_integer('Option 1: 1 Aircraft Carrier, 2 Battleships, 3 Submarines, 4 Cruisers\n'
                                 'Option 2: 1 Aircraft Carrier, 1 Battleship, 2 Submarines, 3 Cruisers\n'
                                 'Option 3: 1 Battleship, 2 Submarines, 3 Cruisers, 4 Boats\n'
                                 '\nSelect an option: ')
        return option

def define_fleet(size, option):
    if size == 5:
        if option == 1:
            return {'Aircraft Carrier': 0, 'Battleships': 1, 'Submarines': 1, 'Cruisers': 0, 'Boats': 1}
        elif option == 2:
            return {'Aircraft Carrier': 0, 'Battleships': 0, 'Submarines': 1, 'Cruisers': 2, 'Boats': 0}
        elif option == 3:
            return {'Aircraft Carrier': 0, 'Battleships': 0, 'Submarines': 0, 'Cruisers': 2, 'Boats': 2}
    else:
        if option == 1:
            return {'Aircraft Carrier': 1, 'Battleships': 2, 'Submarines': 3, 'Cruisers': 4, 'Boats': 0}
        elif option == 2:
            return {'Aircraft Carrier': 1, 'Battleships': 1, 'Submarines': 2, 'Cruisers': 3, 'Boats': 0}
        elif option == 3:
            return {'Aircraft Carrier': 0, 'Battleships': 1, 'Submarines': 2, 'Cruisers': 3, 'Boats': 4}

def define_computer_level():
    print("\nChoose the difficulty level you want")
    print("\n1. The computer chooses randomly")
    print("2. The computer chooses strategically\n")
    level = get_integer("Enter 1 or 2: ")
    return level

def define_mode():
    print("\nChoose a game mode:")
    print("\n1. Alternating mode: players take turns until reaching a number of shots each player entered at the start")
    print("2. Continuous mode: players shoot as long as they hit opponent ships.\nIf they miss, it's the other player's turn.\nThe game ends when one player sinks the opponent's entire fleet.\n")
    mode = get_integer("Enter 1 or 2: ")
    return mode
