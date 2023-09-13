We have a direction service class which helps our Map app to calculate the Estimated Time of Arrival or ETA
and enables it to suppose the best direction.

So DirectionService class must have two methods:
+ calculate_eta()
+ get_direction()

and we want it to support at least three Travel Modes:
+ Driving
+ Walking
+ Bicycling

and in implementation you should consider that the probability to increasing the supported travel methods.