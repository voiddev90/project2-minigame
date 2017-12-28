import pygame
class Acorn(object):

    def __init__(self, x, height):
        self.image = pygame.image.load("images/acorn.png")
        self.moveSpeed = 10
        self.maxHeight = height
        self.rect = self.image.get_rect().move(x, -100)
        
    def getPosition(self):
        return (self.rect.x, self.rect.y)
    
    def getImage(self):
        return self.image

    def moveDown(self):
            self.rect.y += self.moveSpeed

    def offScreen(self):
        if self.rect.y >= self.maxHeight:
            return True
        return False

    def is_collided_with(self, player):
        return self.rect.colliderect(player.rect)

    def render(self, screen):
        screen.blit(self.image, self.rect)