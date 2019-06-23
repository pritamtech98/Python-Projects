import pygame
import time
import random

pygame.init()

crashed = False
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pritam game')

img = pygame.image.load('car.png')
details = img.convert()
# print(details.get_width(), details.get_height())
# game_sound = pygame.mixer.Sound()
game_music = pygame.mixer.music
game_music.load('E://Microsoft Windows XP Startup Sound.wav')

def show_car(x, y):
    gameDisplay.blit(img, (x, y))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
black_color = (53, 115, 255)
green = (0, 255, 0)

x_change = 0
y_change = 0
car_speed = 0
clock=pygame.time.Clock()

def show_buttons(x, y, xw, yh, ac, ic, text, action=None):
    global crashed
    myFont = pygame.font.SysFont(None, 35)
    myText = myFont.render(text, True, black)
    textSurface = myText.get_rect()
    textSurface.center = ((x + xw/2), (y + yh/2))

    pygame.draw.rect(gameDisplay, ic, [x, y, xw, yh])
    gameDisplay.blit(myText, textSurface)
    mousePos = pygame.mouse.get_pos()
    mouseClick = pygame.mouse.get_pressed()

    if ((mousePos[0] < x+xw) and mousePos[0] > x) and ((mousePos[1] < y+yh) and mousePos[1] > y):
        pygame.draw.rect(gameDisplay, ac, [x, y, xw, yh])
        gameDisplay.blit(myText, textSurface)

        if mouseClick[0] != 0 and action != None:
            action()
            crashed=False
    else:
        pygame.draw.rect(gameDisplay, ic, [x, y, xw, yh])
        gameDisplay.blit(myText, textSurface)



def message_display(text):
    our_font = pygame.font.Font('freesansbold.ttf', 100)
    textSurface = our_font.render(text, True, black)
    textRect = textSurface.get_rect()
    textRect.center = (display_width/2, display_height/2)

    gameDisplay.blit(textSurface, textRect)
    pygame.display.update()

    time.sleep(2)
    game_loop()

collided = 0
def detect_collision(count=0):
    font = pygame.font.SysFont(None, 26)
    msg = font.render("Your score : "+str(count), True, black_color)
    gameDisplay.blit(msg, (0, 0))

def quitgame():
    pygame.quit()
    quit()

def front_end():
    global crashed
    frontend = True
    while frontend:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                frontend = False

        gameDisplay.fill(white)
        game_name = 'Pritam Game'
        myFont = pygame.font.Font('freesansbold.ttf', 80)
        game_name2 = myFont.render(game_name, True, black)
        textRect = game_name2.get_rect()
        textRect.center = (display_width/2, display_height/4)

        gameDisplay.blit(game_name2, textRect)
        show_buttons(150, 400, 90, 60, (132, 249, 132), (103, 226, 12), 'Start', game_loop)
        show_buttons(540, 400, 90, 60, (255, 128, 0), red, 'Quit', quitgame)

        pygame.display.update()
        clock.tick(16)

def crash(text):
    coGame = True
    gameDisplay.fill(white)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        font = pygame.font.Font('freesansbold.ttf', 100)
        myText = font.render(text, True, black)
        textRect = myText.get_rect()
        textRect.center = (display_width/2, display_height/4)
        gameDisplay.blit(myText, textRect)

        show_buttons(150, 400, 90, 60, (132, 249, 132), (103, 226, 12), 'Start Again', game_loop)
        show_buttons(540, 400, 90, 60, (255, 128, 0), red, 'Quit', quitgame)

        pygame.display.update()
        clock.tick(20)

def draw_object(objX, objY, objW, objH):
    pygame.draw.rect(gameDisplay, red, [objX, objY, objW, objH])

def game_loop():
    global crashed, x_change
    collided=0
    x = display_width * .2
    y = display_height * .6
    car_width = 240

    objX = random.randrange(0, display_width)
    objY = 0
    oby_speed = 3
    objW = 100
    objH = 100

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash('Quit ?')

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -13
                if event.key == pygame.K_RIGHT:
                    x_change = 13


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            x += x_change

        gameDisplay.fill(white)
        draw_object(objX, objY, objW, objH)
        objY += oby_speed
        show_car(x, y)
        detect_collision(collided)

        if x > display_width - car_width or x < 0:
            crash('You Crashed')
        if objY > display_height:
            objY = 0 - display_height
            objX = random.randrange(0, display_width)
            collided += 1
            oby_speed += oby_speed*.2
            objW += objW*.1


        if y < (objY + objH) and y > objY:
            if (x < objX + objW and x > objX) or (x + car_width > objX and x < objX):
                # message_display('Game Over')
                crash('Game Over')

        pygame.display.update()
        clock.tick(60)




front_end()
# game_loop()
# pygame.quit()
# quit()