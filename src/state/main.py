# here is a demo
from state.bicycling import Bicycling
from state.direction_service import DirectionService
from state.driving import Driving
from state.walking import Walking

ds = DirectionService()
ds.travel_mode = Walking()
ds.calculate_eta()
ds.get_direction()

ds.travel_mode = Driving()
ds.calculate_eta()
ds.get_direction()

ds.travel_mode = Bicycling()
ds.calculate_eta()
ds.get_direction()
