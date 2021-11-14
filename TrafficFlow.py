""" Defines a singular flow of external traffic into the system during a given interval.
Includes tick rates to release cars, generates cars, and passes them into the system."""
import numpy as np
import random
import KeyConstants
class TrafficFlow:
    def __init__( self, start_time, end_time, car_wait_time, entrance_relativity, entrance_names):
        self.start_time = start_time
        self.end_time = end_time
        self.cars_wait_time = car_wait_time
        self.entrance_relativity = entrance_relativity
        self.entrance_names = entrance_names
        generate_traffic()
    """Generates a random distribition of traffic at given time according to relative flows"""
    def generate_traffic(self):
        self.arrival_times= []
        start_t = start_time
        while t < end_time:
            wait_time= np.random.exponential(self.cars_wait_time)
            t+= wait_time
            arrival_times.append((wait_time, choose_random_entrance))
    def tick(self):
        if len(arrival_times) == 0:
            return None
        self.arrival_times[0][0] -= KeyConstants.TICK_RATE
        if self.arrival_times[0][0] < 0:
            #Deals with 'tick overkill'
            if len(arrival_times) >= 2:
                self.arrival_times[1][0] += self.arrival_times[0][0]
            self.arrival_times.pop(0)
            return self.arrival_times[0][1]

    def choose_random_entrance(self):
        return random.choices(self.entrance_names, self.entrance_relativity)


