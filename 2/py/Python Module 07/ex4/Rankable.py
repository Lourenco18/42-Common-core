from abc import ABC, abstractmethod


class Rankable(ABC):

    @abstractmethod
    def get_rank(self):
        pass
