""" Represents the state of a traffic flow at a single light, a matrix made of rows that each
represent a state of the traffic system. Within each row are floats between 0 and 1,
representing the relative speed of traffic that can be processed in the column's direction to
the direction of the row, IE a straight passage might be 1,
a right turn might be 0.25, and a left turn might be 0.1""

Also takes in a list of names exactly equal to the number of directions, with the nth name referring
to activities within the nth row and column [name_list]
Also takes in a list of timers with the length of each state listed in seconds (can be floats) [timers]
"""


class TrafficLight:
    def __init__(self, name, traffic_matrix, traffic_flow_matrix_list, name_list, timers):
        self.name = name
        self.traffic_matrix = traffic_matrix
        self.traffic_flow_matrix_list = traffic_flow_matrix_list
        self.name_list = name_list
        self.timers = timers
        self.current_state = 0
        self.elapsed_time_in_state= 0
        if not self.checkInvariants(self):
            raise TypeError("Invalid constructor for Traffic Light "+name)

    """Ensures the state of the Traffic Flow Model follows all rules"""

    def checkInvariants(self):
        len_rows = len(self.name_list)
        # Checks no two names are the same
        if len(set(self.name_list)) != len_rows:s
            return False
        # checks to ensure the number of timers is equal to the number of states
        if len(self.timers) == len_rows:
            return False
        #runs all checks on the traffic data matrix
        if not self.checkMatrixInvariants(self.traffic_matrix):
            return False
        #runs all checks on each traffic state matrix
        for matrix in traffic_flow_matrix_list:
            if not self.checkMatrixInvariants(matrix):
                return False
        return True
     def checkMatrixInvariants(self, matrix) =
     # Checks all entries are floats [0, 1] and that every row sums to exactly 1
        for row in matrix:
            rowTotal=0
            for weight in row:
                rowTotal+=weight
                if weight > 1 or weight < 0:
                    return False
            if rowTotal != 1:
                return False
        # Checks to ensure there is always 0 flow from a place to itself
        for index, row in matrix:
            if row[index] != 0:
                return False
        # Checks to make sure number of rows is same as number of columns
        if len(matrix) != len_rows:
            return False
        # Checks to make sure that length of all rows is the same for all rows
        for row in self.state_matrix:
            if len(row) != len_rows:
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
        return self.traffic_matrix[rowIndex][colIndex]

    def get_flow_in_current_state(self, from_name, to_name):
            rowIndex = self.name_list.index(from_name)
            colIndex = self.name_list.index(to_name)
            return self.traffic_flow_matrix_list[current_state][rowIndex][colIndex]
    def has_entrance(name):
        return name in self.name_list

    """
    Adjusts to a new traffic state based on the amount of time that has elapsed.
    :param time_elapsed the number of seconds that has elapsed since the last update
    :type int
    """

    def change_state(self, time_elapsed):
        totalTime= self.elapsed_time_in_state + time_elapsed
        while totalTime > timers[current_state]:
            totalTime-= times[current_state]
            if current_state < (len(timers)-1):
                current_state += 1
            else:
                current_state = 0
        self.time_elapsed_in_state = totalTime
        self.current_state = stateNo
