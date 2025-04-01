# 🚪 Evacuation Simulation

## 📌 Description

This project simulates an evacuation process where individuals in a room attempt to reach an exit while adhering to specific movement constraints. The simulation follows a step-by-step progression, ensuring that only one person exits per step and that individuals navigate around obstacles efficiently.

---

## 🎯 Rules of the Simulation

1. **Movement Restrictions**:
   - Each person can move one step per turn.
   - A person can move **up, down, left, or right** if the space is unoccupied and not an obstacle.
   - No diagonal movements are allowed.
   - A person **cannot move into a space occupied by another person**.

2. **Exit Conditions**:
   - Only **one person can exit per step**.
   - The exit is located at a **designated door position**.
   - A person must be **at the door position** to exit.

3. **Obstacles**:
   - Obstacles can be placed anywhere in the room at specified coordinates. These obstacles are not passable, and people cannot move through them.
   - The door **cannot be blocked by obstacles**.

4. **Evacuation Order**:
   - People will move toward the exit if they can, prioritizing spaces closer to the door.
   - **One person can exit at a time**, and others will continue to move until they reach the exit or are blocked by other individuals or obstacles.

5. **Room Dimensions**:
   - The room is represented as a grid with **N rows** and **M columns**.
   - People can be randomly placed in the room, but they cannot occupy the same space as obstacles or the exit.

---

## 🧩 Parameters

Here are the key parameters of the simulation:

1. **Number of People (`N`)**:
   - The total number of people to simulate in the room. The number must be less than or equal to the room's total capacity, excluding spaces blocked by obstacles.
   - **Default**: `30`

2. **Room Size (`n` x `m`)**:
   - `n`: Number of rows in the room.
   - `m`: Number of columns in the room.
   - **Default**: `8x7` grid

3. **Door Position (`door_row`, `door_col`, `door_width`)**:
   - `door_row`: The row where the door is located.
   - `door_col`: The column where the door is located.
   - `door_width`: The width of the door (how many adjacent spaces the door occupies).
   - **Default values**:
     - `door_row = 0`
     - `door_col = 2`
     - `door_width = 1` (a door spanning 1 space in the top row).

4. **Obstacles**:
   - You can place obstacles anywhere in the room at specific coordinates. These obstacles are not passable, and people cannot move through them.
   - **Important**: Obstacles **cannot block the door**. Ensure obstacles are placed away from the door area.

---


## 🧑‍🤝‍🧑 Further Studies

It would be interesting to **study evacuation times** depending on the number and positioning of obstacles in the room. Varying the obstacle setup (e.g., the density of obstacles or their proximity to the door) could reveal how different room layouts impact evacuation efficiency.

Key areas for further research include:
- **Effect of Obstacle Density**: Investigate how the number of obstacles affects evacuation time.
- **Obstacle Placement**: Study if placing obstacles near the door slows evacuation, or if there is a critical threshold where movement becomes severely restricted.
- **Room Configuration**: Examine how the size or shape of the room influences evacuation speed with varying obstacle configurations.

These insights could help determine **the most optimal room configurations** for efficient evacuations.


## 🧑‍🤝‍🧑 Improvements and Future Work

Potential improvements for this simulation include:
- **Dynamic Behavior**: Enhance the logic for people’s movements, allowing them to change direction based on nearby obstacles or other people.
- **Speed Adjustment**: Add an option to control the simulation's speed, enabling more granular observation of the evacuation process.
- **Visualization Enhancements**: Implement a graphical user interface (GUI) or animation for better visualization of the room and evacuation process.
- **Data Collection**: Track and record evacuation data (e.g., time per person, steps taken) to analyze patterns and optimize room layouts.

These improvements would help make the simulation more interactive and provide more detailed insights into the evacuation dynamics.

