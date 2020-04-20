import math
import pygame


class GUI:
    def __init__(self, grid, path, size):
        self.path = path

        # colors
        white = (255, 255, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        green = (0, 170, 0)
        blue = (0 , 0, 255)
        width = 750 / size - 1
        height = 750 / size - 1
        margin = 1

        pygame.init()
        gameDisplay = pygame.display.set_mode((750, 750))
        pygame.display.set_caption('AStar!')
        gameDisplay.fill(white)

        finished = False
        gameClock = pygame.time.Clock()

        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (width + margin)
                    row = pos[1] // (width + margin)
                    grid[row][column] = 1
                    print("Click ", pos, "Grid coordinates: ", row, column)

            # Set the screen background
            gameDisplay.fill(black)

            # Draw the grid
            for row in range(size):
                for column in range(size):
                    color = white
                    if grid[row][column] == 1:
                        color = black
                    if (row, column) in path:
                        color = green
                    if (row, column) == path[0]:
                        color = blue
                    if (row, column) == path[-1]:
                        color = red
                    pygame.draw.rect(gameDisplay, color, [(margin + width) * column + margin, (margin + height) * row +
                                                          margin, width, height])

            gameClock.tick(60)
            pygame.display.flip()

        pygame.quit()
