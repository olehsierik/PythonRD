import abc


class Animal(abc.ABC):
    Voice: str = None

    @abc.abstractmethod
    def speak(self) -> str:
        pass


class Dog(Animal):
    Voice: str = 'Woof'

    def speak(self) -> str:
        return self.Voice


class Cat(Animal):
    Voice: str = 'Meow'

    def speak(self) -> str:
        return self.Voice


class Horse(Animal):
    Voice: str = 'Neigh'

    def speak(self) -> str:
        return self.Voice
