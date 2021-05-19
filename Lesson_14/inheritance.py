from abc import ABC, abstractmethod


class WaterBird(ABC):
    def __init__(self, name):
        self.name = name
        print('Bird is {}'.format(self.name))

    def where_is_live(self):
        print('On the Earth')

    def swim(self):
        print('Can swim very fast')

    @abstractmethod
    def voice(self):
        # raise NotImplementedError('Method Voice need to over')
        pass


class Penguin(WaterBird):
    def __init__(self, name):
        WaterBird.__init__(self, name)
        print('Penguin is ready')

    def where_is_live(self):
        print('South pole')

    def run(self):
        print('Run fast')

    def voice(self):
        print('Pi-pi-pi')


class Duck(WaterBird):
    def __init__(self, name):
        super().__init__(name)
        print('Duck is ready')

    def where_is_live(self):
        print('Anywhere')

    def fly(self):
        print('Fly very high')

    def voice(self):
        print('Kra-kra-kra')


ping = Penguin('Ping')
ping.where_is_live()
ping.swim()
ping.run()
ping.voice()

duck = Duck('Donald')
duck.where_is_live()
duck.swim()
duck.fly()
duck.voice()
