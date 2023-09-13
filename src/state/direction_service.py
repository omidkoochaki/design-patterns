from state.travel_mode import TravelMode


class DirectionService:
    _travel_mode: TravelMode = None

    def calculate_eta(self):
        self.travel_mode.calculate_eta()

    def get_direction(self):
        self.travel_mode.get_direction()

    @property
    def travel_mode(self):
        return self._travel_mode

    @travel_mode.setter
    def travel_mode(self, value):
        self._travel_mode = value