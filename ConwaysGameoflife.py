print("Sanio Frederic,1AY24AI099,SEC-O")
import random
import time
import os

WIDTH = 40
HEIGHT = 20

def create_grid():
    return [[random.choice([0, 1]) for _ in range(WIDTH)] for _ in range(HEIGHT)]

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(''.join(['■' if cell else ' ' for cell in row]))

def get_neighbor_count(grid, x, y):
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = (x + dx) % WIDTH, (y + dy) % HEIGHT
            count += grid[ny][nx]
    return count

def next_generation(grid):
    new_grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbors = get_neighbor_count(grid, x, y)
            if grid[y][x] == 1:
                new_grid[y][x] = 1 if neighbors in [2, 3] else 0
            else:
                new_grid[y][x] = 1 if neighbors == 3 else 0
    return new_grid

def main():
    grid = create_grid()
    try:
        while True:
            print_grid(grid)
            grid = next_generation(grid)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nGame of Life stopped.")

if __name__ == "__main__":
    main()
