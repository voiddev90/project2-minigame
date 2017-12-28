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

Player = Player.Player((screenRect[2] / 3), (screenRect[3] // 2) +200, width)
Acorn = Acorn.Acorn(300, screenRect[3])
# AcornImage = pygame.image.load(Acorn.getImage())

gameActive = True

def movement():
    global gameActive
    keyDown = pygame.key.get_pressed()
    pygame.key.set_repeat(1,50)
    if keyDown[pygame.K_d or keyDown[pygame.K_RIGHT]]:
        Player.moveRight()
    elif keyDown[pygame.K_a] or keyDown[pygame.K_LEFT]:
        Player.moveLeft()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameActive = False

# def hitAcorn(player, acorn):
    
#     if acorn.is_collided_with(player):
#         print("hit")

while gameActive:
    movement()
    Acorn.moveDown()
    screen.fill(black)
    Player.render(screen)
    Acorn.render(screen)
    if Acorn.is_collided_with(Player):
        print("Hit")
        # Acorn.kill()
    clock.tick(30)
    pygame.display.flip()