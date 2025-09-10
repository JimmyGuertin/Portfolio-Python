# main.py

from simulation import simulate_evacuation

# ===========================
# 🎯 Configuration
# ===========================

N = 30         # Number of people
n = 8          # Number of rows
m = 7          # Number of columns
door_row = 0   # Door row position
door_col = 2   # Door column position
door_width = 1 # Door width

# Obstacles in the room (modifiable)
obstacles = {(3, 3), (4, 4)}

if __name__ == "__main__":
    # Run the evacuation simulation
    print(simulate_evacuation(N, n, m, door_row, door_col, door_width, obstacles))
