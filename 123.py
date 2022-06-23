import pygame
import random
import math
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((1280, 720))

# Back
background = pygame.image.load('download.png')

# Back sound
mixer.music.load('Game music.mp3')
mixer.music.play(-1)
# later background will be menu and enemies will be running among desks


# Title and Icon
pygame.display.set_caption('Kubstu 19-ITK9-PO2')
icon = pygame.image.load('spaceship (1).png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('9h8v3nj8iWE.jpg')
playerX = 640
playerY = 580
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6

xyz = 0

for i in range(num_of_enemies):
    enemyX.append(random.randint(150, 950))
    enemyY.append(random.randint(1, 100))
    enemyX_change.append(8)
    enemyY_change.append(75)
    xyz += 1
    enemyImg.append(pygame.image.load(f'{xyz}.jpg'))
    # split 1.jpg to 1 and jpg then convert 1 into integer
    # and add 1 then turn it back into string and load([i].jpg)

# Bullet
# Ready = bullet not seen
# Fire - bullet moving

bulletImg = pygame.image.load('diagram (3).png')
bulletX = 0
bulletY = 580
bulletX_change = 0
bulletY_change = 25
bullet_state = 'ready'

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 42)

textX = 10
textY = 10

# GG TEXT
over_font = pygame.font.Font('freesansbold.ttf', 72)

# blit = draw


def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render('GAME OVER', True, (0, 0, 0))
    screen.blit(over_text, (450, 300))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x, y))


def icollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2))))
    if distance < 27:
        return True
    else:
        return False


# Main_loop
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -14
            if event.key == pygame.K_RIGHT:
                playerX_change = +14
            if event.key == pygame.K_e:
                if bullet_state == 'ready':
                    # Get coordinate
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Boundaries
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1136:
        playerX = 1136

    # Enemy movement
    for i in range(num_of_enemies):

        #GG
        if enemyY[i] > 600:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 8
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 1100:
            enemyX_change[i] = -8
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = icollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480  # maybe change it
            bullet_state = 'ready'
            score_value += 1
            enemyX[i] = random.randint(0, 1200)
            enemyY[i] = random.randint(50, 100)

        enemy(enemyX[i], enemyY[i], i)

    # BulMovement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()