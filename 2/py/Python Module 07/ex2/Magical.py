from abc import ABC, abstractmethod


class Magical(ABC):

    @abstractmethod
    def cast_spell(self):
        pass
