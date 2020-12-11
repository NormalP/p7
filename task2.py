from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def consumption(self):
        return int(self.param / 6.5 + 0.5)


class Costume(Clothes):
    def consumption(self):
        return int(2 * self.param + 0.3)





coat = Coat(409)
costume = Costume(55)
print(f'Для пошива пальто нужно: {coat.consumption():.2f} ткани')
print(f'Для пошива костюма нужно: {costume.consumption():.2f}  ')
print(f'Для пошива всего нужно {(coat.consumption() + costume.consumption())} ткани')
