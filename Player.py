import pygame
class Player(object):

    def __init__(self, startX, StartY, width):
        self.lifes = 3
        self.moveSpeed = 10
        self.maxWidth = (width - 200)
        self.image = pygame.image.load("images/player1-left.png")
        self.rect = self.image.get_rect().move(startX, StartY)

    
    def getPosition(self):
        return (self.rect.x, self.rect.y)

    def isPlayerAlive(self):
        if self.lifes > 0:
            return True
        return False

    def moveLeft(self):
        self.image = pygame.image.load("images/player1-left.png")
        if self.rect.x > 0:
            self.rect.x -= self.moveSpeed
            
    def moveRight(self):
        self.image = pygame.image.load("images/player1-right.png")
        if self.rect.x < self.maxWidth:
            self.rect.x += self.moveSpeed
    
    def decreaseLife(self):
        self.lifes -= 1

    def render(self, screen):
        screen.blit(self.image, self.rect)