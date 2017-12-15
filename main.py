import pygame
import sys
import Player
import Acorn


pygame.init()

size = width, height = 1080, 1080
black = 255,255,255

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

player = Player.Player()
playerImage = pygame.image.load(player.getImage())
gameActive = True
Acorn = Acorn.Acorn(300, 200)
AcornImage = pygame.image.load(Acorn.getImage())

while gameActive:
    keyDown = pygame.key.get_pressed()
    pygame.key.set_repeat(1,50)
    if keyDown[pygame.K_d]:
        player.moveRight()
    if keyDown[pygame.K_a]:
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
    clock.tick(60)
    print(player.getPosition())
    pygame.display.flip()