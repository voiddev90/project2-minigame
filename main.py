import pygame
import sys
from Player import Player
from Acorn import Acorn
from random import randint


pygame.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

size = width, height = 1200, 800
background = pygame.image.load("images/background.jpg")
backgroundRect = background.get_rect()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
screenRect = screen.get_rect()
winTime = 120000
spawnTime = 2000

player = Player((screenRect[2] / 3), (screenRect[3] // 2) +200, width)

gameActive = True
acorns = []
lastSpawn = 0
wonGame = False

def moveAcorns():
    global acorns
    global screen
    newList = []
    for acorn in acorns:
        acorn.moveDown()
        acorn.render(screen)
        if not collided(acorn) and not acorn.offScreen():
            newList.append(acorn)
    acorns = newList

def spawnAcorn():
    global acorns, width, height, lastSpawn
    randomPoint = randint(0, (width - 200))
    if (randomPoint - lastSpawn) <= 10:
        randomPoint += 30
    acorns.append(Acorn(randomPoint, height))
    lastSpawn = randomPoint

def collided(acorn):
    global player
    if acorn.isCollidedWith(player):
        player.decreaseLife()
        return True
    return False

def movement():
    global gameActive
    keyDown = pygame.key.get_pressed()
    pygame.key.set_repeat(1,50)
    if keyDown[pygame.K_d or keyDown[pygame.K_RIGHT]]:
        player.moveRight()
    elif keyDown[pygame.K_a] or keyDown[pygame.K_LEFT]:
        player.moveLeft()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameActive = False

while gameActive:
    screen.fill((255,255,255))
    screen.blit(background, backgroundRect)
    if not wonGame:
        movement()
        player.render(screen)
        moveAcorns()
        now = pygame.time.get_ticks()
        screen.blit(font.render('Lifes: ' + str(player.lifes),  False, (0,0,0)), (0,0))
        if len(acorns) < 5 and (now - lastSpawn) >= spawnTime:
            spawnAcorn()
            lastSpawn = now
        if now == winTime:
            wonGame = True
    else:
        screen.blit(font.render('Gewonnen!',  False, (0,0,0)), (0,0))
    clock.tick(30)
    pygame.display.flip()