from abc import ABC, abstractmethod


class GameStrategy(ABC):

    @abstractmethod
    def choose_action(self, deck):
        pass
