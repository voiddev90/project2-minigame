
class Player(object):

    def __init__(self):
        self.lifes = 3
        self.image = "images/player.png"
        self.posX = 450
        self.posY = 850
        self.moveSpeed = 10

    
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
        if self.posX < 900:
            self.posX += self.moveSpeed
    
    def decreaseLife(self):
        self.lifes -= 1