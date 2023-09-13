from abc import ABC, abstractmethod


class TravelMode(ABC):
    @abstractmethod
    def calculate_eta(self):
        pass

    @abstractmethod
    def get_direction(self):
        pass
