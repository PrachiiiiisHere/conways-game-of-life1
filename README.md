# Conway's Game of Life

A simple implementation of Conway's Game of Life built using Python and Pygame.

## Screenshot

![Conway's Game of Life](screenshot.png)

## About the Project

Conway's Game of Life is a cellular automaton devised by mathematician John Conway in 1970.

The simulation consists of a grid of cells where each cell can be either:

* Alive (1)
* Dead (0)
The state of the grid evolves over time according to a small set of rules based on the number of living neighbors surrounding each cell.

### Rules
1. Any live cell with fewer than 2 live neighbors dies.
2. Any live cell with 2 or 3 live neighbors survives.
3. Any live cell with more than 3 live neighbors dies.
4. Any dead cell with exactly 3 live neighbors becomes alive.

Despite these simple rules, complex and interesting patterns can emerge over time.

## Features
* Randomly generated starting grid
* Conway's Game of Life rules implementation
* Real-time simulation using Pygame
* Adjustable simulation speed using `clock.tick()`

## Technologies Used
* Python
* Pygame

## What I Learned
While building this project, I practiced:

* Working with 2D grids
* Nested loops
* List comprehensions
* Functions
* Pygame rendering
* Simulation and game loop concepts
* Applying Conway's Game of Life rules.

## Run the Project
Install Pygame:
    pip install pygame

Run the program:
    python game.py

