class Acorn(object):

    def __init__(self, x, y):
        self.image = "images/eikel.png"
        self.posX = x
        self.posY = y
        self.moveSpeed = 5

    
    def getPosition(self):
        return (self.posX, self.posY)
    
    def getImage(self):
        return self.image

    def moveDown(self):
        self.posY += self.moveSpeed