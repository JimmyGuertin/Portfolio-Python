# display.py

def display_room(room, door_row, door_col, door_width, obstacles):
    """Displays the room with symbols for better visualization."""
    (n, m) = room.shape
    display = ""

    for i in range(n):
        for j in range(m):
            if (i, j) in obstacles:
                display += "🟥 "  # Obstacle
            elif door_row == 0 and i == 0 and door_col <= j < door_col + door_width:
                display += "🚪 "  # Top door
            elif door_row == n - 1 and i == n - 1 and door_col <= j < door_col + door_width:
                display += "🚪 "  # Bottom door
            elif door_col == 0 and j == 0 and door_row <= i < door_row + door_width:
                display += "🚪 "  # Left door
            elif door_col == m - 1 and j == m - 1 and door_row <= i < door_row + door_width:
                display += "🚪 "  # Right door
            elif room[i, j] == 1:
                display += "👤 "  # Person
            else:
                display += "⬜ "  # Empty space
        display += "\n"

    print(display)
