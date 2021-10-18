""" Represents the state of a traffic flow at a single light, a matrix made of rows that each
represent a state of the traffic system. Within each row are floats between 0 and 1,
representing the relative speed of traffic that can be processed in the column's direction to
the direction of the row, IE a straight passage might be 1,
a right turn might be 0.25, and a left turn might be 0.1""

Also takes in a list of names exactly equal to the number of directions, with the nth name refferring
to activities within the nth row and column [name_list]
Also takes in a list of timers with the length of each state listed in seconds (can be floats) [timers]
"""


class TrafficFlowModel:
    def __init__(self, state_matrix, name_list, timers):
        self.state_matrix = state_matrix
        self.name_list = name_list
        self.timers = timers
        self.current_state = 0
        if not self.checkInvariants(self):
            raise TypeError("Invalid constructor for Traffic Flow Model")

    """Ensures the state of the Traffic Flow Model follows all rules"""

    def checkInvariants(self):
        # Checks to make sure that length of all rows is the same for all rows
        len_rows = len(self.name_list)
        for row in self.state_matrix:
            if len(row) != len_rows:
                return False
        # Checks to make sure number of rows is same as number of columns
        if len(self.state_matrix) != len_rows:
            return False
        # Checks that the number of columns is equal to number of rows
        if len(self.state_matrix[0]) != len_rows:
            return False
        # Checks all entries are floats [0, 1]
        for row in self.state_matrix:
            for weight in row:
                if weight > 1 or weight < 0:
                    return False
        # Checks no two names are the same
        if len(set(self.name_list)) != len_rows:
            return False
        # Checks to ensure there is always 0 flow from a place to itself
        for index, row in self.state_matrix:
            if row[index] != 0:
                return False
        # checks to ensure the number of timers is equal to the number of states
        if len(self.timers) == len_rows:
            return False
        return True

    """
    :param from_name: the name of the place traffic is flowing from
    :type string
    :param to_name: the name of the place traffic is flowing to
    :type string
    :return A number between 0 and 1 representing the factor by which traffic
     is scaled going in this direction
    :rtype float
    """

    def get_traffic_flow(self, from_name, to_name):
        rowIndex = self.name_list.index(from_name)
        colIndex = self.name_list.index(to_name)
        return self.state_matrix[rowIndex][colIndex]

    """
    :param stateNo the number of the state that the light is currently in
    :type int
    """

    def change_state(self, stateNo):
        if stateNo > len(self.name_list):
            return False
        self.current_state = stateNo
