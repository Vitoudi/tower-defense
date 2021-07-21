import pygame
import datetime

class Enemy:
    velocity = 5
    posX = 0
    __is_active = False
    __observers = []
    __already_left_screen = False

    def __init__(self, window, color, width, height) -> None:
        self.window = window
        self.posY = -width
        self.color = color
        self.__width = width
        self.__height = height

    def register_observer(self, obs):
        self.__observers.append(obs)

    def check_if_leave_screen(self):
        surface = pygame.display.get_surface()
        surface_height = surface.get_height()
        leave_screen = self.posY > surface_height
        return leave_screen

    def handle_screen_leave(self):
        self.__already_left_screen = True
        print(self.__observers)
        for observer in self.__observers:
            print("calling observer")
            if not hasattr(observer, "on_enemy_leave_screen"): continue
            observer.on_enemy_leave_screen()
    
    def move_forword(self):
        self.__is_active = True

        if self.__already_left_screen: return

        did_leave_screen = self.check_if_leave_screen()

        if did_leave_screen:
            self.handle_screen_leave()

        self.posY += self.velocity
        self.draw()

    def stopMoving(self):
        self.__is_moving = False

    def get_width(self):
        return self.__width

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.posX, self.posY, self.__width, self.__height))