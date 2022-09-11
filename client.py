import pygame as p

from data import boardWidth, boardHeight, getClock
from game import createGame


def updateDisplay():
    p.display.flip()


class Programme:
    def __init__(self, player='white'):
        p.init()

        self.boardWidth = boardWidth
        self.boardHeight = boardHeight
        self.maxFPS = 60
        self.clock = getClock()

        self.screen = self.initScreen()

        self.player = player

        self.game = createGame(player=self.player)

        self.running = True

    def reset(self):
        self.clock = getClock()

        self.player = 'white' if self.player == 'black' else 'black' if self.player == 'white' else 'white'

        self.game = createGame(player=self.player)

    def runCycle(self):
        self.manageEvents()
        self.game.draw(self.screen)
        self.clock.tick(self.maxFPS)
        updateDisplay()

    def initScreen(self):
        return p.display.set_mode((self.boardWidth, self.boardHeight))

    def fillScreen(self, color):
        self.screen.fill(color)

    def manageEvents(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                self.running = False

            elif event.type == p.KEYDOWN:
                if event.key == p.K_r:
                    self.reset()
