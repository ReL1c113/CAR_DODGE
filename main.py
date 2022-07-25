import pygame
import math
import random
import time


tracking=time.time()

pygame.init()

screen = pygame.display.set_mode((600, 800))

pygame.display.set_caption("CAR GAME")
numb_of_car = 3
time_added=0

background = pygame.image.load('car_background.jpg')
l1 = [20, 120, 220, 320, 420, 520]
background_height = background.get_height()
scroll = 0
pannel = math.ceil(800 / background_height) + 2



# PLAYER
playerImg = pygame.image.load('car (4).png')
player_x = 220
player_y = 700
change_px = 0

# ENEMY_1
e1Img = pygame.image.load('car.png')
e1_x = random.choice(l1)
e1_y = random.randint(-100, -50)
change_e1 = 0.6

# ENEMY_2
e2Img = pygame.image.load('car (1).png')
e2_x = random.choice(l1)
e2_y = random.randint(-200, -140)
change_e2 = 0.6

# ENEMY 3
e3Img = pygame.image.load('car (2).png')
e3_x = random.choice(l1)
e3_y = random.randint(-300, -240)
change_e3 = 0.6

# ENEMY 4
e4Img = pygame.image.load('car (3).png')
e4_x = random.choice(l1)
e4_y = random.randint(-500, -340)
change_e4 = 0.6

# ENEMY 5
e5Img = pygame.image.load('car (1)r.png')
e5_x = random.choice(l1)
e5_y = random.randint(-100, -50)
change_e5 = 0.6

# ENEMY 6
e6Img = pygame.image.load('carr.png')
e6_x = random.choice(l1)
e6_y = random.randint(-400, -320)
change_e6 = 0.6


# ENEMY CAR USER DEFINED FUNCTIONS
def e1(x, y):
    screen.blit(e1Img, (x, y))


def e2(x, y, ):
    screen.blit(e2Img, (x, y))


def e3(x, y):
    screen.blit(e3Img, (x, y))


def e4(x, y, ):
    screen.blit(e4Img, (x, y))


def e5(x, y):
    screen.blit(e5Img, (x, y))


def e6(x, y):
    screen.blit(e6Img, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


# COLLISION USER DEFINED FUNCTIONS
def isCollision(x, y, z, w):
    distance = math.sqrt((math.pow((x - z), 2)) + (math.pow((y - w), 2)))
    if distance <= 30:
        return True
    else:
        return False




run = True
while (run):
    time_added=time_added+0.00001
    for i in range(pannel):
        screen.blit(background, (0, i * background_height + scroll - background_height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_px = -0.5
            if event.key == pygame.K_RIGHT:
                change_px = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                change_px = 0
            if event.key == pygame.K_RIGHT:
                change_px = 0
    player_x = change_px + player_x
    # ENEMY CAR MVEMENT
    e1_y = e1_y + change_e1 +time_added
    e3_y = e3_y + change_e3 +time_added
    e2_y = e2_y + change_e2 +time_added
    e4_y = e4_y + change_e4 +time_added
    e5_y = e5_y + change_e5 +time_added
    e6_y = e6_y + change_e6 +time_added
    # ENEMY CAR RESPAWNING
    if e1_y >= 900:
        e1_x = random.choice(l1)
        e1_y = random.randint(-100, -50)

    if e3_y >= 900:
        e3_x = random.choice(l1)
        e3_y = random.randint(-300, -240)

    if e2_y >= 900:
        e2_x = random.choice(l1)
        e2_y = random.randint(-300, -240)

    if e4_y >= 900:
        e4_x = random.choice(l1)
        e4_y = random.randint(-300, -240)

    if e5_y >= 900:
        e5_x = random.choice(l1)
        e5_y = random.randint(-300, -240)

    if e6_y>=900:
        e6_x=random.choice(l1)
        e6_y=random.randint(-400,-320)
    # BOUNDARY FOR OUR PLAYER
    if player_x >= 520:
        player_x = 520
    if player_x <= 20:
        player_x = 20
    # COLLISION CHECK
    collision1 = isCollision(player_x, player_y, e1_x, e1_y)
    if collision1:
        break
    collision2 = isCollision(player_x, player_y, e3_x, e3_y)
    if collision2:
        break
    collision3 = isCollision(player_x, player_y, e2_x, e2_y)
    if collision3:
        break
    collision4 = isCollision(player_x, player_y, e4_x, e4_y)
    if collision4:
        break
    collision5 = isCollision(player_x, player_y, e5_x, e5_y)
    if collision5:
        break
    collision6 = isCollision(player_x, player_y, e6_x, e6_y)
    if collision6:
        break

    # ENEMY CAR FINAL POSITION
    e1(e1_x, e1_y)
    e3(e3_x, e3_y)
    e2(e2_x, e2_y)
    e4(e4_x, e4_y)
    e5(e5_x, e5_y)
    e6(e6_x, e6_y)
    # PLAYER FINAL POSITION
    player(player_x, player_y)

    scroll = scroll + 0.4
    if abs(scroll) > background_height:
        scroll = 0
    pygame.display.update()
print(tracking/100000)
