import numpy as np
from display import display_room

def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    """Calculate Manhattan distance between two points."""
    return abs(x1 - x2) + abs(y1 - y2)

def move_toward_exit(room: np.ndarray, door_row: int, door_col: int, door_width: int, obstacles: list[tuple[int, int]]) -> tuple[np.ndarray, bool]:
    """
    Move all people closer to the exit if possible.
    Only one person exits per step and avoids obstacles.
    """
    (n, m) = np.shape(room)
    new_room = np.copy(room)
    moved = False  
    exit_occurred = False  # Track if someone has exited this step
    
    # Define door positions
    door_positions = [(door_row, j) for j in range(door_col, door_col + door_width)]
    
    for i in range(n):
        for j in range(m):
            if room[i, j] == 1:  # Person detected
                moves = []

                # Possible moves (up, down, left, right)
                possible_moves = [
                    (i - 1, j) if i > 0 and (i - 1, j) not in obstacles and new_room[i - 1, j] == 0 else None,
                    (i + 1, j) if i < n - 1 and (i + 1, j) not in obstacles and new_room[i + 1, j] == 0 else None,
                    (i, j - 1) if j > 0 and (i, j - 1) not in obstacles and new_room[i, j - 1] == 0 else None,
                    (i, j + 1) if j < m - 1 and (i, j + 1) not in obstacles and new_room[i, j + 1] == 0 else None
                ]
                
                moves = [move for move in possible_moves if move is not None]
                
                # Exit if person is at the door
                if not exit_occurred and (i, j) in door_positions:
                    new_room[i, j] = 0
                    moved = True
                    exit_occurred = True
                    continue
                
                # Move toward closest door
                if moves and not exit_occurred:
                    best_move = min(moves, key=lambda move: min(manhattan_distance(move[0], move[1], d[0], d[1]) for d in door_positions))
                    new_room[i, j] = 0
                    new_room[best_move[0], best_move[1]] = 1
                    moved = True

    return new_room, moved

def is_empty(room: np.ndarray) -> bool:
    """Check if the room is fully evacuated."""
    return np.all(room == 0)

def simulate_evacuation(N: int, n: int, m: int, door_row: int, door_col: int, door_width: int, obstacles: list[tuple[int, int]]) -> str:
    """Simulate the evacuation process and display each step."""
    room = np.zeros((n, m), dtype=int)

    # Randomly place people in the room
    placed_people = 0
    while placed_people < min(N, n * m - len(obstacles) - door_width):
        i, j = np.random.randint(0, n), np.random.randint(0, m)
        if room[i, j] == 0 and (i, j) not in obstacles and (i, j) not in [(door_row, dj) for dj in range(door_col, door_col + door_width)]:
            room[i, j] = 1
            placed_people += 1

    print("\n🚪 **Evacuation Simulation** 🚪")
    print(f"📍 Door Location: Row {door_row}, Column {door_col} (Width: {door_width})")
    print(f"👥 Number of People: {N}")
    print(f"🟥 Obstacles: {obstacles if obstacles else 'None'}\n")

    print("🏠 **Initial Room State:**")
    display_room(room, door_row, door_col, door_width, obstacles)

    T = 0

    while not is_empty(room):
        room, moved = move_toward_exit(room, door_row, door_col, door_width, obstacles)
        if moved:
            T += 1
            print(f"\n⏳ **Step {T}:**")
            display_room(room, door_row, door_col, door_width, obstacles)

    print("\n✅ **Final Room State:** (Fully Evacuated)")
    display_room(room, door_row, door_col, door_width, obstacles)
    return f"\n🏁 **Evacuation completed in {T} seconds!**"
