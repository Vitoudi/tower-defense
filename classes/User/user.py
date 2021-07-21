import pygame

class User:
    posY = 50
    posX = 50
    width = 200
    height = 200

    def __init__(self, window) -> None:
        self.window = window

    def onGameStart(self):
        """ self.draw() """

    def onNewEvent(self, event):
        # print(event)
        """ if event.type == pygame.MOUSEMOTION:
            self.posX = event.pos[0] - (self.width / 2)
            self.posY = event.pos[1]- (self.height / 2)
            self.draw() """

    def draw(self):
        self