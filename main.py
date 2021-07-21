from classes.evntLopp.EventLoop import EventLoop
from classes.Game.game import Game
import pygame
pygame.init()

window = pygame.display.set_mode((700, 700))

event_loop = EventLoop(window)
game = Game(window, event_loop)

game.start()
