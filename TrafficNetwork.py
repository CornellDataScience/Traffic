"""Represents the state of the traffic network. Includes a list of TrafficLights, and a matrix of
    connections from the lights to other lights

    The connection_matrix is a matrix n x n where n is the length of the traffic_light_list,
    each element will store a connection light a to light b or Null meaning there is no direct connection
"""
import TrafficLight
import Connection
import KeyConstants
class TrafficNetwork:
    def __init__(self, traffic_light_list, connection_list):
        self.traffic_light_list = traffic_light_list
        self.connection_matrix = connection_list
        self.global_time = 0
        self.cars_waiting = []
        if not self.checkInvariants(self):
            raise TypeError("Invalid constructor for Traffic Model")
    def checkInvariants(self):
        #checks that matrix is n x 2.
        for row in self.connection_matrix:
            if len(row) != 2:
                return False
        return True
    def tick_movements(self):
        self.global_time += KeyConstants.TICK_RATE
        exiting_traffic = []
        for light in self.traffic_lights:
            exit = light.tick(self.global_time)
            if exit != None:
                exiting_traffic.append(exit)
        # This likely has pretty garbage O(n^2) time complexity. Look to optimize if going larger scale
        for exit in exiting_traffic:
            connection = self.get_connection_with_exit(exit)
            if connection != None:
                self.put_car(connection)
    def tick_cars_waiting(self):
        for car in self.cars_waiting:
            car[1] -= KeyConstants.TICK_RATE
        cars_completed = [x for x in self.cars_waiting if x[1] <= 0]
        self.cars_waiting = [x for x in self.cars_waiting if x[1] > 0]
        #Bad time complexity
        for car in cars_completed:
            for light in self.traffic_light_list:
                if light.has_entrance(car[0]):
                    light.put_car_in(car[0])
                    break
            raise RuntimeError("No light found with given entrance " + car[0])


    def put_car(self, connection):
        tuple = (connection.entrance_name, connection.get_wait_time())
        self.cars_waiting.append(tuple)


    def get_connection_with_exit(self, exit):
        for connection in self.connection_matrix:
            if connection.exit_name == exit:
                return connection
        return None

    def tick(self):
        self.tick_movements()
        self.tick_cars_waiting()





