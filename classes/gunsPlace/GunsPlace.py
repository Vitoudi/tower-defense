import pygame
from enum import Enum     # for enum34, or the stdlib version
# from aenum import Enum  # for the aenum version
Pos = Enum('Pos', 'LEFT RIGHT')


class GunsPlace:
    color = (100, 100, 100)

    def __init__(self, window, posX: Pos) -> None:
        self.window = window
        self.posX = posX
        surface = self.__get_surface()
        self.__height = surface.get_height()
        self.__width = (surface.get_width() * 20) / 100

    def __get_surface(self):
        surface = pygame.display.get_surface()
        return surface

    def __get_left_pos(self):
        return 0

    def __get_right_pos(self):
        surface = pygame.display.get_surface()
        surface_width = surface.get_width()

        return surface_width - self.__width

    def __get_pos(self):
        if self.posX == Pos.LEFT:
            return self.__get_left_pos()
        return self.__get_right_pos()

    def onNewFrame(self):
        self.draw()

    def draw(self):
        pos = self.__get_pos()
        pygame.draw.rect(self.window, self.color, (pos, 0, self.__width, self.__height))