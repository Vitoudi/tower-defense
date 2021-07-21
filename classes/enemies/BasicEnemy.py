from classes.enemies.Enemy import Enemy


class BasicEnemy(Enemy):
    __observers = []
    color = (255, 0, 0)
    width = 50
    height = 50

    def __init__(self, window) -> None:
        super().__init__(width=self.width, height=self.height, color=self.color, window=window)

    def register_observer(self, obs):
        self.__observers.append(obs)

