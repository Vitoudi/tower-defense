import pygame


class EventLoop:
    observers = []

    def __init__(self, window) -> None:
        self.window = window

    def register_observer(self, observer):
        self.observers.append(observer)

    def start(self):
        run = True

        while run:
            pygame.time.delay(50)

            for observer in self.observers:
                if hasattr(observer, "onNewFrame"): observer.onNewFrame()

            pygame.display.update()
            self.window.fill((0, 0, 0))
            
            for event in pygame.event.get():
                for observer in self.observers:
                    if hasattr(observer, "onNewEvent"): observer.onNewEvent(event)

                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()
