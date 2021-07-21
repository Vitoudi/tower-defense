from classes.enemies.Enemy import Enemy
import random
from classes.enemies.BasicEnemy import BasicEnemy
from classes.enemies.GrungeEnemy import GrungeEnemy

class EnemyFactory:
    __weak_enemies = [BasicEnemy, GrungeEnemy]
    __regular_enemies = []
    __strong_enemies = []

    def __init__(self, window) -> None:
        self.window = window

    def __get_random_enemy_for(self, enemy_list: list[Enemy]):
        random_index = random.randrange(0, len(enemy_list))
        Random_enemy = enemy_list[random_index]
        return Random_enemy(self.window)

    def get_random_weak_enemy(self) -> Enemy:
        random_weak_enemy = self.__get_random_enemy_for(self.__weak_enemies)
        return random_weak_enemy