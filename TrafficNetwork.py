"""Represents the state of the traffic network. Includes a list of TrafficLights, and a matrix of
    connections from the lights to other lights

    The connection_matrix is a matrix n x n where n is the length of the traffic_light_list,
    each element will store a connection light a to light b or Null meaning there is no direct connection
"""
import TrafficLight
import Connection
class TrafficNetwork:
    def __init__(self, traffic_light_list, connection_matrix):
        self.traffic_light_list = traffic_light_list
        self.connection_matrix = connection_matrix
        if not self.checkInvariants(self):
            raise TypeError("Invalid constructor for Traffic Model")
    def checkInvariants(self):
        #checks that matrix is n x n.
        for row in connection_matrix:
            if len(row) != len(connection_matrix):
                return False
        #check that no light connects to itself
        for index, row in enumerate(connection_matrix):
            if row[index] != null:
                return False
        #check every connection
        for row in matrix:
            for connection in row:
                if not checkConnection(connection):
                    return False
        return True
    def checkConnection(connection):
        if connection == null:
            return True
        #TODO: check lights have proper names once functionality is available





