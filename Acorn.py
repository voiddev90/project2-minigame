class Acorn(object):

    def __init__(self, x, height):
        self.image = "images/eikel.png"
        self.posX = x
        self.posY = 0
        self.moveSpeed = 10
        self.maxHeight = height

    
    def getPosition(self):
        return (self.posX, self.posY)
    
    def getImage(self):
        return self.image

    def moveDown(self):
            self.posY += self.moveSpeed

    def offScreen(self):
        if self.posY >= self.maxHeight:
            return True
        return False