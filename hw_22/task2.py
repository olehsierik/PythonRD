import abc


class Animal(abc.ABC):
    voice: str = None

    @abc.abstractmethod
    def speak(self) -> str:
        pass


class Dog(Animal):
    voice: str = 'Woof'

    def speak(self) -> str:
        return self.voice


class Cat(Animal):
    voice: str = 'Meow'

    def speak(self) -> str:
        return self.voice


class Horse(Animal):
    voice: str = 'Neigh'

    def speak(self) -> str:
        return self.voice
