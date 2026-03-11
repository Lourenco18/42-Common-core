from abc import ABC, abstractmethod


class CardFactory(ABC):

    @abstractmethod
    def create_creature(self):
        pass

    @abstractmethod
    def create_spell(self):
        pass
