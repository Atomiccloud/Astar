import random
import sys

from AStar import astar
from DisplayGUI import GUI


def make_grid(size, percent):
    grid = []
    grid = [[0 for x in range(size)] for y in range(size)]
    if percent != 0:
        percent = percent/100
        grid = fill_grid(grid, size, percent)
    return grid


def fill_grid(grid, size, percent):
    obstacleCount = int(round(size*size*percent))

    for i in range(obstacleCount):
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if grid[x][y] != 1 and (x, y) != (1, 1) and (x, y) != (size-2, size-2):
            grid[x][y] = 1
        else:
            i -= 1

    return grid


def main():
    user_input = 0

    user_input = input('Type 1 for 50x50, 2 for 100x100, 3 for 200x200 or 4 for 300x300. Type quit to exit: ')
    if user_input != '1':
        try:
            percent = int(input('What percent of the grid should be filled with obstacles? (10-90): '))
        except:
            print('Invalid number')
            sys.exit()

    if user_input == '1':
        size = 25
        percent = 50
    elif user_input == '2':
        size = 100
    elif user_input == '3':
        size = 200

    elif user_input == '4':
        size = 300
    elif user_input == 'quit':
        print('Have A Good Day!')
    else:
        print('Invalid Selection. I cannnot handle this. Good bye')
        sys.exit()

    start = (1, 1)
    end = (size - 2, size - 2)
    grid = make_grid(size, percent)
    path = astar(grid, start, end, size)

    # for x in grid:
    #     print(*x, sep=" ")

    if path:
        print(f'path found: {path}')
        GUI(grid, path, size)
    else:
        print('Path not found')


if __name__ == '__main__':
    main()
