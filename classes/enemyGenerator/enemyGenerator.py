from classes.EnemyFactory.EnemyFactory import EnemyFactory
from classes.enemies.Enemy import Enemy
import random
import pygame

class EnemyGenerator:
    __ENEMY_GENERATION_RATE = 50
    __current_frame_num_in_generation_cycle = 0
    __is_generating = False
    active_enemies = []

    def __init__(self, window, enemy_factory: EnemyFactory) -> None:
        self.enemy_factory = enemy_factory
        self.window = window

    def check_if_is_time_to_generate_new_enemy(self):
        if self.__current_frame_num_in_generation_cycle == self.__ENEMY_GENERATION_RATE:
            self.__current_frame_num_in_generation_cycle = 0
            return True
        return False

    def __get_ramdom_starting_point(self, enemy):
        enemy_width = enemy.get_width()
        surface = pygame.display.get_surface()
        surface_width = surface.get_width()

        randomX = random.randrange(0, surface_width - enemy_width)

        return randomX

    def on_game_start(self):
        self.__is_generating = True
        self.generate_new_enemy()

    def generate_new_enemy(self):
        enemy = self.enemy_factory.get_random_weak_enemy()
        enemy.posX = self.__get_ramdom_starting_point(enemy)
        enemy.draw()
        self.active_enemies.append(enemy)
        print("registering as observer")
        enemy.register_observer(self)

        num_of_enemies = len(self.active_enemies)
        # print("num of enemies after append: " + str(num_of_enemies))

    def on_enemy_leave_screen(self):
        # print("left screen -> deleting first")
        num_of_enemies = len(self.active_enemies)
        # print("num of enemies: " + str(num_of_enemies))
        if num_of_enemies > 0:
            del self.active_enemies[0]

    def move_enemies(self):
        for enemy in self.active_enemies:
            enemy.move_forword()

    def onNewFrame(self):
        self.__current_frame_num_in_generation_cycle += 1
        is_time_to_generate_enemy = self.check_if_is_time_to_generate_new_enemy()

        self.move_enemies()

        if is_time_to_generate_enemy:
            # print("is time")
            self.generate_new_enemy()



            

        

        

        
