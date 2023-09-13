from state.travel_mode import TravelMode


class Bicycling(TravelMode):
    def calculate_eta(self):
        print("calculating ETA for Bicycling")

    def get_direction(self):
        print("getting direction for Bicycling")
