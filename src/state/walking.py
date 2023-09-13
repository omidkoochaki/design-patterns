from state.travel_mode import TravelMode


class Walking(TravelMode):
    def calculate_eta(self):
        print("calculating ETA for Walking")

    def get_direction(self):
        print("getting direction for Walking")
