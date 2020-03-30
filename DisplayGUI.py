import time
import pygame


class GUI:
    def __init__(self, path, vertex, permDisplay, u_input):
        self.path = path
        self.vertex = vertex

        pygame.init()

        # colors
        white = (255, 255, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        green = (75, 255, 50)

        gameDisplay = pygame.display.set_mode((900, 540))
        pygame.display.set_caption('Smarter than turtle')
        gameDisplay.fill(white)

        size = pygame.display.get_surface().get_size()
        gridXSize = size[0] // 30
        gridYSize = size[1] // 18

        x = [gridXSize * x for x in range(30)]
        y = [gridYSize * y for y in range(18)]
        v = []
        for point in vertex:
            x = point[0] * gridXSize
            y = point[1] * gridYSize
            v.append((x, y))

        if u_input == '1':
            pygame.draw.polygon(gameDisplay, black, (v[0], v[1], v[2], v[3]), 4)
            pygame.draw.polygon(gameDisplay, black, (v[4], v[5], v[6], v[7], v[8]), 4)
            pygame.draw.polygon(gameDisplay, black, (v[9], v[10], v[11]), 4)
            pygame.draw.polygon(gameDisplay, black, (v[12], v[13], v[14], v[15]), 4)
            pygame.draw.polygon(gameDisplay, black, (v[16], v[17], v[18], v[19]), 4)
            pygame.draw.polygon(gameDisplay, black, (v[20], v[21], v[22], v[23]), 4)
            pygame.draw.polygon(gameDisplay, black, (v[24], v[25], v[26]), 4)
            pygame.draw.polygon(gameDisplay, black, (v[27], v[28], v[29], v[30], v[31], v[32]), 4)

            # start dot and font
            pygame.draw.circle(gameDisplay, green, (30, 420), 5)
            font = pygame.font.SysFont('Arial', 20, True)
            startText = font.render('Start', True, black)
            gameDisplay.blit(startText, (10, 420))

            # end
            pygame.draw.circle(gameDisplay, red, (870, 31), 5)
            startText = font.render('End', True, black)
            gameDisplay.blit(startText, (865, 5))
        else:
            pygame.draw.polygon(gameDisplay, black, (v[0], v[1], v[2], v[3], v[4]), 4)
            pygame.draw.polygon(gameDisplay, black, (v[5], v[6], v[7], v[8]), 4)
            pygame.draw.polygon(gameDisplay, black, (v[9], v[10], v[11], v[12]), 4)
            pygame.draw.polygon(gameDisplay, black, (v[13], v[14], v[15], v[16], v[17]), 4)
            pygame.draw.polygon(gameDisplay, black, (v[18], v[19], v[20]), 4)

            # start dot and font
            pygame.draw.circle(gameDisplay, green, (60, 150), 5)
            font = pygame.font.SysFont('Arial', 20, True)
            startText = font.render('Start', True, black)
            gameDisplay.blit(startText, (50, 140))

            # end
            pygame.draw.circle(gameDisplay, red, (750, 330), 5)
            startText = font.render('End', True, black)
            gameDisplay.blit(startText, (745, 330))



        #path
        p = []
        for point in path:
            x = point[0] * gridXSize
            y = point[1] * gridYSize
            p.append((x, y))
        color = red
        if permDisplay:
            color = green
        pygame.draw.lines(gameDisplay, color, False, p, 4)
        pygame.display.update()
        time.sleep(1)

        if permDisplay:
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    pygame.display.update()

