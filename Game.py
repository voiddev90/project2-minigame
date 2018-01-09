import pygame
import sys
import os
from Player import Player
from Acorn import Acorn
from random import randint
class Game():

    def __init__(self):
        pygame.init()
        self.folder = os.path.dirname(__file__)
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.winFont = pygame.font.SysFont('Comic Sans MS', 50)

        self.size = self.width, self.height = 1200, 800
        self.background = pygame.image.load(self.folder + "/images/background.jpg")
        self.backgroundRect = self.background.get_rect()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size)
        self.screenRect = self.screen.get_rect()
        self.winTime = 120000
        # self.winTime = 5000
        self.spawnTime = 2000

        self.player = Player((self.screenRect[2] / 3), (self.screenRect[3] // 2) +200, self.width)

        self.gameActive = True
        self.acorns = []
        self.lastSpawn = 0
        self.stopGame = False
        self.gameWon = False

    def isGameWon(self):
        return self.gameWon
    
    def moveAcorns(self):
        newList = []
        for acorn in self.acorns:
            acorn.moveDown()
            if not self.collided(acorn) and not acorn.offScreen():
                newList.append(acorn)
        self.acorns = newList
    
    def collided(self, acorn):
        if acorn.isCollidedWith(self.player):
            self.player.decreaseLife()
            return True
        return False

    def spawnAcorn(self):
        randomPoint = randint(0, (self.width - 200))
        if (randomPoint - self.lastSpawn) <= 10:
            randomPoint += 30
        self.acorns.append(Acorn(randomPoint, self.height))
        self.lastSpawn = randomPoint
    
    def renderAcorns(self):
        for acorn in self.acorns:
            acorn.render(self.screen)
    
    def movement(self):
        if not self.stopGame:
            keyDown = pygame.key.get_pressed()
            pygame.key.set_repeat(1,50)
            if keyDown[pygame.K_d] or keyDown[pygame.K_RIGHT]:
                self.player.moveRight()
            elif keyDown[pygame.K_a] or keyDown[pygame.K_LEFT]:
                self.player.moveLeft()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.stopGame:
                    self.gameActive = False
    
    def runGame(self):
        while self.gameActive:
            self.screen.fill((255,255,255))
            self.screen.blit(self.background, self.backgroundRect)
            self.movement()
            self.screen.blit(self.font.render('Lifes: ' + str(self.player.lifes),  False, (0,0,0)), (0,0))
            now = pygame.time.get_ticks()
            if not self.stopGame:
                self.moveAcorns()
                if len(self.acorns) < 5 and (now - self.lastSpawn) >= self.spawnTime:
                    self.spawnAcorn()
                    self.lastSpawn = now
            if not self.player.isPlayerAlive():
                self.stopGame = True
                self.screen.blit(self.winFont.render('Geen levens meer! Druk op escape om terug te gaan',  False, (0,0,0)), (200,400))        
            elif now > self.winTime:
                self.stopGame = True
                self.gameWon = True
                self.screen.blit(self.winFont.render('Sleutel gevonden! Druk op escape om door te gaan',  False, (0,0,0)), (200,400))
                

            self.clock.tick(30)
            self.player.render(self.screen)
            self.renderAcorns()
            pygame.display.flip()
        return self.gameWon