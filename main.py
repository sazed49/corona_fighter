import pygame
import sys
import random
import math
from pygame import mixer

pygame.init()
# create the screen
WIDTH = 800
player_size=50
enemy_size=50
HEIGHT = 600
# rgb color
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
yellow=(255,255,0)
clock = pygame.time.Clock()
# font for score
myFont = pygame.font.SysFont("monospace", 35)
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 50)
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('b.png')
mixer.music.load('background.wav')
mixer.music.play(-1)
# game loop
# title and icon
pygame.display.set_caption("corona fighter")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
# player
playerimg = pygame.image.load('doctor.png')
 # ready mane bullet dekha jabena

font = pygame.font.Font('freesansbold.ttf', 32)
testx = 10
texty = 10
over_font = pygame.font.Font('freesansbold.ttf', 64)
def game_intro():
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

        screen.fill(white)
        message_to_screen("Welcome to Corona Fighter",
                          green,
                          -100,
                          "large")
        message_to_screen("The objective of the game is to kill corona virus",
                          black,
                          -30)

        message_to_screen("The more virus you shoot, the more you score",
                          black,
                          10)

        message_to_screen("If virus touches you, you die!",
                          black,
                          50)

        message_to_screen("Press C to play, P to pause or Q to quit.",
                          black,
                          180)

        pygame.display.update()
        clock.tick(15)





def pause(x):
    paused = True
    if x==1:
        message_to_screen("won",
                          black,
                          -100,
                          size="large")
        message_to_screen("Press C to continue or Q to quit.",
                          black, 25)
    else:
        message_to_screen("Paused",
                          white,
                          -100,
                          size="large")

        message_to_screen("Press C to continue or Q to quit.",yellow
                          ,
                          25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        # gameDisplay.fill(white)

        clock.tick(5)













def is_collision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx, 2)) + (math.pow(enemyy - bullety, 2)))
    if distance < 27:
        return True
    else:
        return False

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (WIDTH/ 2), (HEIGHT / 2) + y_displace
    screen.blit(textSurf, textRect)

def game_loop():
    game_over=False
    game_exit=False
    playerx=370
    playery = 520
    player_pos = [playerx,playery ]
    playerx_change = 0

    # enemy
    enemyimg = []
    enemyx=[]
    enemyy=[]

    enemyx_change = []
    enemyy_change = []
    num_of_enemy =6
    score_value=0
    # bullet
    bullet = pygame.image.load('hospital.png')
    bulletx = 0
    bullety = 480
    bukketx_change = 0
    bullety_change = 5
    bullet_state = "ready"
    c=num_of_enemy
    for i in range(num_of_enemy):
        enemyimg.append(pygame.image.load('virus.png'))
        enemyx.append(random.randint(0, 735))  # 0 theke 800 porjnoto position er random value ber korbe
        enemyy.append(random.randint(20, 150))
        enemyx_change.append(2)
        enemyy_change.append(40)

    while not game_exit:
        if game_over == True:
            message_to_screen("Game over",
                              red,
                              y_displace=-50,
                              size="large")

            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size="medium")
            pygame.display.update()
        while game_over == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over= False
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()
        screen.fill((0, 0, 0))  # background color
        # background
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerx_change = -5
                if event.key == pygame.K_SPACE:
                        b=1
                        bullet_sound = mixer.Sound('laser.wav')
                        bullet_sound.play()
                        bulletx = playerx
                        bullety-=0.1
                        bullet_state = "fire"
                        screen.blit(bullet, (bulletx + 16, bullety + 10))
                if event.key == pygame.K_RIGHT:
                    playerx_change = 5
                if event.key == pygame.K_p:
                    pause(2)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerx_change = 0

        playerx += playerx_change
        # checking boundary of player
        if playerx <= 0:
            playerx = 0
        elif playerx >= 736:
            playerx = 736
        # checking boundary of enemy

        for i in range(num_of_enemy):

            if enemyy[i] >400:
                for j in range(num_of_enemy):
                    enemyy[j] = 2000

                break

            enemyx[i] += enemyx_change[i]
            if enemyx[i] <= 0:
                enemyx_change[i] = 2
                enemyy[i] += enemyy_change[i]
            elif enemyx[i] >= 736:
                enemyx_change[i] = -2
                enemyy[i] += enemyy_change[i]
            # collision
            collision = is_collision(enemyx[i], enemyy[i], bulletx, bullety)

            if collision:
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                bullety = 480
                bullet_state = "ready"
                score_value += 1

                enemyx[i] = random.randint(0, 736)
                enemyy[i] = random.randint(50, 150)




            screen.blit(enemyimg[i], (enemyx[i], enemyy[i]))
        # bullet movement
        if bullety <= 40:
            bullety = 480
            bullet_state = "ready"
        if bullet_state is "fire":
            bullet_state = "fire"
            screen.blit(bullet, (bulletx + 16, bullety + 10))
            bullety -= bullety_change

        screen.blit(playerimg, (playerx, playery))
        score = font.render("score:" + str(score_value), True, (255, 0, 0))
        ascore = font.render("press P to pause", True, (255, 255, 0))

        screen.blit(score, (testx, texty))
        screen.blit(ascore, (testx, texty+50))
        pygame.display.update()  # eta thakbei.karon display te jai change kori last a update func call kora lagbe jate update hoy change gula
    pygame.quit()
    quit()
game_intro()
game_loop()
