import pygame

# Initialize the game
pygame.init()
pygame.font.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF, 32)
screen.fill((255, 255, 255, 128))  # notice the alpha value in the color

turn = 'X'
rects = []
rects_type = ['', '', '', '', '', '', '', '', '']

running = True


def drawRect():
    rectWidth = width / 3
    rectHeight = height / 3

    for i in range(3):
        for j in range(3):
            rects.append(pygame.draw.rect(screen, pygame.Color(100, 100, 100),
                                          pygame.Rect(i * rectWidth, j * rectHeight, rectWidth, rectHeight), 2, 0))


def drawTextInRect():
    for i in range(9):
        # draw text
        if rects_type[i] != '':
            if rects_type[i] == 'X':
                color = pygame.Color(0, 100, 0)
            else:
                color = pygame.Color(100, 0, 0)

            font = pygame.font.Font(None, 150)
            text = font.render(rects_type[i], True, color)
            # text_rect = text.get_rect(center=(width / 6, height / 6))
            text_rect = text.get_rect(center=rects[i].center)
            screen.blit(text, text_rect)


def changeTurn():
    global turn

    if turn == 'X':
        turn = 'O'
    elif turn == 'O':
        turn = 'X'


def check_win():
    for i in range(9):
        if rects_type[0] != '' and rects_type[0] == rects_type[1] == rects_type[2]:
            pygame.draw.line(screen, pygame.Color(250, 250, 0), rects[0].center, rects[2].center, 10)
            drawEndScreen()
            return False

        if rects_type[3] != '' and rects_type[3] == rects_type[4] == rects_type[5]:
            pygame.draw.line(screen, pygame.Color(250, 250, 0), rects[3].center, rects[5].center, 10)
            drawEndScreen()
            return False

        if rects_type[6] != '' and rects_type[6] == rects_type[7] == rects_type[8]:
            pygame.draw.line(screen, pygame.Color(250, 250, 0), rects[6].center, rects[8].center, 10)
            drawEndScreen()
            return False

        if rects_type[0] != '' and rects_type[0] == rects_type[3] == rects_type[6]:
            pygame.draw.line(screen, pygame.Color(250, 250, 0), rects[0].center, rects[6].center, 10)
            drawEndScreen()
            return False

        if rects_type[1] != '' and rects_type[1] == rects_type[4] == rects_type[7]:
            pygame.draw.line(screen, pygame.Color(250, 250, 0), rects[1].center, rects[7].center, 10)
            drawEndScreen()
            return False

        if rects_type[2] != '' and rects_type[2] == rects_type[5] == rects_type[8]:
            pygame.draw.line(screen, pygame.Color(250, 250, 0), rects[2].center, rects[8].center, 10)
            drawEndScreen()
            return False

        if rects_type[0] != '' and rects_type[0] == rects_type[4] == rects_type[8]:
            pygame.draw.line(screen, pygame.Color(250, 250, 0), rects[0].center, rects[8].center, 10)
            drawEndScreen()
            return False

        if rects_type[2] != '' and rects_type[2] == rects_type[4] == rects_type[6]:
            pygame.draw.line(screen, pygame.Color(250, 250, 0), rects[2].center, rects[6].center, 10)
            drawEndScreen()
            return False

        if rects_type[0] != '' and rects_type[1] != '' and rects_type[2] != '' and \
                rects_type[3] != '' and rects_type[4] != '' and rects_type[5] != '' and \
                rects_type[6] != '' and rects_type[7] != '' and rects_type[8] != '':
            drawEndScreen(tie=True)
            return False

    return True


def drawEndScreen(tie=False):
    s = pygame.Surface((width / 6 * 4, height / 6 * 4), pygame.SRCALPHA)  # per-pixel alpha
    s.fill((255, 255, 255, 128))  # notice the alpha value in the color
    screen.blit(s, (width / 6, height / 6))

    if tie:
        text = 'It is a TIE'
    else:
        text = 'Game Over'

    back_rect = pygame.Rect(rects[0].center[0], rects[0].center[1], width / 6 * 4, height / 6 * 4)
    rect = pygame.draw.rect(s, pygame.Color(200, 200, 200, 128), back_rect)

    font = pygame.font.Font(None, 50)
    text = font.render(text, True, pygame.Color(0, 0, 0))
    text_rect = text.get_rect(center=[screen.get_rect().center[0], screen.get_rect().center[1] - 50])
    screen.blit(text, text_rect)

    text = font.render('Try again (y/n)?', True, pygame.Color(0, 0, 0))
    text_rect = text.get_rect(center=[screen.get_rect().center[0], screen.get_rect().center[1] + 50])
    screen.blit(text, text_rect)


# Keep loading through
while 1:
    screen.fill(0)  # clear the screen before drawing it again

    drawRect()
    drawTextInRect()
    running = check_win()

    pygame.display.flip()  # update the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if running:
                for i in range(9):
                    if rects[i].collidepoint(pos):
                        if rects_type[i] == '':
                            rects_type[i] = turn
                            changeTurn()

        if not running:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    turn = 'X'
                    rects = []
                    rects_type = ['', '', '', '', '', '', '', '', '']
                if event.key == pygame.K_n:
                    pygame.quit()
