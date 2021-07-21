from classes.enemies.Enemy import Enemy

class GrungeEnemy(Enemy):
    __observers = []
    color = (255, 115, 0)
    width = 30
    height = 60

    def __init__(self, window) -> None:
        print(f"intern obs: {self.__observers}")
        super().__init__(width=self.width, height=self.height, color=self.color, window=window)

    def register_observer(self, obs):
        self.__observers.append(obs)