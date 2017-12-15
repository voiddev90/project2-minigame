import pygame
class Player(object):

    def __init__(self, startX, StartY, width):
        self.lifes = 3
        self.image = "images/player.png"
        self.posX = startX
        self.posY = StartY
        self.moveSpeed = 10
        self.maxWidth = (width - 200)

    
    def getPosition(self):
        return (self.posX, self.posY)
    
    def getImage(self):
        return self.image

    def getLifes(self):
        return self.lifes

    def isPlayerAlive(self):
        if self.lifes > 0:
            return True
        return False

    def moveLeft(self):
        if self.posX > 0:
            self.posX -= self.moveSpeed
    def moveRight(self):
        if self.posX < self.maxWidth:
            self.posX += self.moveSpeed
    
    def decreaseLife(self):
        self.lifes -= 1