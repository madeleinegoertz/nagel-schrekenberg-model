# Stolen from Wikipedia https://en.wikipedia.org/wiki/Nagel%E2%80%93Schreckenberg_model
# Acceleration: All cars not at the maximum velocity have their velocity increased by one unit. 
#   For example, if the velocity is 4 it is increased to 5.
# Slowing down: All cars are checked to see if the distance between it and the car in front 
#   (in units of cells) is smaller than its current velocity (which has units of cells per time 
#   step). If the distance is smaller than the velocity, the velocity is reduced to the number of
#   empty cells in front of the car – to avoid a collision. For example, if the velocity of a car
#   is now 5, but there are only 3 free cells in front of it, with the fourth cell occupied by 
#   another car, the car velocity is reduced to 3.
# Randomization: The speed of all cars that have a velocity of at least 1, is now reduced by one 
#   unit with a probability of p. For example, if p = 0.5, then if the velocity is 4, it is reduced
#   to 3 50% of the time.
# Car motion: Finally, all cars are moved forward the number of cells equal to their velocity.
#   For example, if the velocity is 3, the car is moved forward 3 cells.

# State variables for a car
# - Current position (cell)
# - Current velocity (measured in cells/delta t)

# State variables for a cell (unit of roadway)
# - boolean of whether or not it's currently occupied by a car.
# Constants
# - Cell that it's immediately behind
# I want to put these in a circular linked list!!

# Time
# - Discretize time to a certain step. 

from lane import *

linked_list = test_list()
