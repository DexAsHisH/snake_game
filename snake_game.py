import pygame
import time
import random

pygame.init()

food_size = 24
block_size = 15
# Frame per seconds
clock = pygame.time.Clock()
FPS = 15


# screen
WIDTH, HEIGHT = 700, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
green = (0, 200, 0)


# Title and icon
pygame.display.set_caption("snake Game!")
icon = pygame.image.load('snake.png')
food = pygame.image.load('food.png')
pygame.display.set_icon(icon)


def snake(snakeList, block_size):
    for XnY in snakeList:
        pygame.draw.rect(win, green, [XnY[0], XnY[1], block_size, block_size])


# Declaring Fonts Size
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 30)
largefont = pygame.font.SysFont("comicsansms", 50)

# Displaying Fonts Size
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)

    elif size == "medium":
        textSurface = medfont.render(text, True, color)

    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurface, textRect = text_objects(msg, color, size)
    textRect.center = (WIDTH/2), (HEIGHT/2) + y_displace
    win.blit(textSurface, textRect)


def pause():
    paused = True

    message_to_screen("Paused", blue, y_displace=-100, size="large")
    message_to_screen("press C to continue or Q to quit.",
                      white, y_displace=25, size="small")
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        # win.fill(black)
        clock.tick(5)


def score(score):
    text = smallfont.render("score: "+str(score), True, red)
    win.blit(text, [0, 0])


def randFood():
    food_x = round(random.randrange(0, WIDTH-food_size))
    food_y = round(random.randrange(0, HEIGHT-food_size))
    return food_x, food_y


def Gameintro():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        win.fill(black)
        message_to_screen("Welcome To Snake World!", green,
                          y_displace=-100, size="large")
        message_to_screen("press C to play, P to Pause or Q to quit",
                          white, y_displace=100, size="medium")

        pygame.display.update()
        clock.tick(15)


def gameLoop():
    gameOver = True
    gameExit = True
    snake_x = WIDTH/2
    snake_y = HEIGHT/2
    change_x = 0
    change_y = 0

    snakeList = []
    snakeLength = 1

    food_x, food_y = randFood()

    while gameExit:
        if gameOver == False:
            message_to_screen("Game Over!", red, y_displace=-50, size="large")
            message_to_screen("press C to play again or Q to quit",
                              white, y_displace=50, size="small")
            pygame.display.update()

        while gameOver == False:
            # win.fill(black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = False
                    gameOver = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = False
                        gameOver = True

                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():                
            if event.type == pygame.QUIT:
                gameExit = False
            
            if event.key == pygame.K_LEFT:
                change_x = -block_size
                change_y = 0

            elif event.key == pygame.K_RIGHT:
                change_x = block_size
                change_y = 0

            elif event.key == pygame.K_UP:
                change_y = -block_size
                change_x = 0

            elif event.key == pygame.K_DOWN:
                change_y = block_size
                change_x = 0

            elif event.key == pygame.K_p:
                pause()

        if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
            gameOver = False

        snake_x += change_x
        snake_y += change_y
        clock.tick(FPS)

        win.fill(black)
        #pygame.draw.rect(win, blue, [food_x, food_y, food_size, food_size])
        win.blit(food, (food_x, food_y))

        snakeHead = []
        snakeHead.append(snake_x)
        snakeHead.append(snake_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for body in snakeList[:-1]:
            if body == snakeHead:
                gameOver = False

        snake(snakeList, block_size)
        score(snakeLength-1)
        pygame.display.update()

        if snake_x > food_x and snake_x < food_x + food_size or snake_x + block_size > food_x and snake_x + block_size < food_x + food_size:
            if snake_y > food_y and snake_y < food_y + food_size:

                food_x, food_y = randFood()
                snakeLength = snakeLength + 1

            elif snake_y + block_size > food_y and snake_y + block_size < food_y + food_size:

                food_x, food_y = randFood()
                snakeLength = snakeLength + 1

    pygame.quit()
    quit()


Gameintro()
gameLoop()
