import pygame
class Player(object):

    def __init__(self, startX, StartY, width):
        self.lifes = 3
        self.image = pygame.image.load("images/player.png")
        self.moveSpeed = 10
        self.maxWidth = (width - 200)
        self.rect = self.image.get_rect().move(startX, StartY)

    
    def getPosition(self):
        return (self.rect.x, self.rect.y)
    
    def getImage(self):
        return self.image

    def getLifes(self):
        return self.lifes

    def isPlayerAlive(self):
        if self.lifes > 0:
            return True
        return False

    def moveLeft(self):
        if self.rect.x > 0:
            self.rect.x -= self.moveSpeed
    def moveRight(self):
        if self.rect.x < self.maxWidth:
            self.rect.x += self.moveSpeed
    
    def decreaseLife(self):
        self.lifes -= 1

    def render(self, screen):
        screen.blit(self.image, self.rect)