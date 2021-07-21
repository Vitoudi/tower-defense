import pygame
from classes.gunsPlace.GunsPlace import GunsPlace, Pos
from classes.EnemyFactory.EnemyFactory import EnemyFactory
from classes.enemies.GrungeEnemy import GrungeEnemy
from classes.enemies.BasicEnemy import BasicEnemy
from classes.enemyGenerator.enemyGenerator import EnemyGenerator
from classes.evntLopp.EventLoop import EventLoop
from classes.User.user import User


class Game:
    enemyGenerator: EnemyGenerator
    guns_place_left: GunsPlace
    guns_place_right: GunsPlace
    observers = []

    def __init__(self, window, event_loop: EventLoop) -> None:
        self.window = window
        self.event_loop = event_loop

    def registerObserver(self, observer):
        self.observers.append(observer)

    def ___register_default_observers(self):
        self.event_loop.register_observer(self.enemyGenerator)
        self.event_loop.register_observer(self.guns_place_left)
        self.event_loop.register_observer(self.guns_place_right)
        self.registerObserver(self.enemyGenerator)

    def __create_instances(self):
        surface = pygame.display.get_surface()
        surface_width = surface.get_width()

        self.guns_place_left = GunsPlace(self.window, Pos.LEFT)
        self.guns_place_right = GunsPlace(self.window, Pos.RIGHT)
        enemyFactory = EnemyFactory(self.window)
        self.enemyGenerator = EnemyGenerator(self.window, enemyFactory)

    def start(self):
        self.__create_instances()

        self.___register_default_observers()

        for observer in self.observers:
            if hasattr(observer, "on_game_start"): observer.on_game_start()

        self.event_loop.start()

