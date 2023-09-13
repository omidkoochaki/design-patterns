from state.travel_mode import TravelMode


class Driving(TravelMode):
    def calculate_eta(self):
        print("calculating ETA for Driving")

    def get_direction(self):
        print("getting direction for Driving")

