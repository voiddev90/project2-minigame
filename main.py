import pygame
import sys
import Player
import Acorn


pygame.init()

size = width, height = 1200, 800
black = 255,255,255

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
screenRect = screen.get_rect()
print()

player = Player.Player((screenRect[2] / 3), (screenRect[3] // 2) +200, width)
playerImage = pygame.image.load(player.getImage())
Acorn = Acorn.Acorn(300, screenRect[3])
AcornImage = pygame.image.load(Acorn.getImage())

gameActive = True

while gameActive:
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
    
    Acorn.moveDown()
    screen.fill(black)
    screen.blit(playerImage, player.getPosition())
    screen.blit(AcornImage, Acorn.getPosition())
    if(Acorn.getPosition()[1] == player.getPosition()[1]):
        print("hit!")
    clock.tick(30)
    pygame.display.flip()