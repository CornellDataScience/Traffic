
""" Represents the state of a traffic flow at a single light, a matrix made of rows that each
represent a state of the traffic system. Within each row are floats between 0 and 1,
representing the relative speed of traffic that can be processed in the column's direction to
the direction of the row, IE a straight passage might be 1,
a right turn might be 0.25, and a left turn might be 0.1""

Also takes in a list of names exactly equal to the number of directions, with the nth name referring
to activities within the nth row and column [name_list]
Also takes in a list of timers with the length of each state listed in seconds (can be floats) [timers]
"""
import TrafficEntrance
import KeyConstants
import random
class TrafficLight:
    def __init__(self, name, traffic_matrix, flow_matrix, entrance_names, traffic_entrance, timers):
        self.name = name
        self.traffic_matrix = traffic_matrix
        self.traffic_entrance = traffic_entrance
        self.entrance_names = entrance_names
        self.timers = timers
        self.flow_matrix = flow_matrix
        self.current_state = 0
        self.current_timer= timers[0]
        self.car_queue = [0 * len(entrance_names)]
        self.is_yellow = False
        if not self.checkInvariants(self):
            raise TypeError("Invalid constructor for Traffic Light "+name)

    """Ensures the state of the Traffic Flow Model follows all rules"""
    def checkInvariants(self):
        len_rows = len(self.entrance_name_list)
        if not self.checkMatrixInvariants(self.traffic_matrix):
            return False
        # runs all checks on each traffic state matrix
        for matrix in [self.traffic_matrix, self.flow_matrix]:
            if not self.checkMatrixInvariants(matrix):
                return False
        # Checks no two names are the same
        if len(set(self.entrance_name_list)) != len_rows:
            return False
        # checks to ensure the number of timers is equal to the number of states
        if len(self.timers) == len_rows:
            return False
        return True
    """
    Checks that the matrix involved follows all invariant rules
    """
    def checkMatrixInvariants(self, matrix):
        # Checks all entries are floats [0, 1] and that every row sums to exactly 1
        len_rows = len(self.entrance_name_list)
        for row in matrix:
            rowTotal = 0
            for weight in row:
                rowTotal += weight
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

    def get_traffic_flow(self, from_name):
        rowIndex = self.entrance_name_list.index(from_name)
        return self.traffic_matrix[rowIndex]
    def get_traffic_state(self, index):
        return self.traffic_matrix[index]
    def get_name_index(self, entrance_name):
        return self.entrance_name_list.index(entrance_name)
    def put_car_in(self,entrance_name):
        self.car_queue[self.get_name_index(entrance_name)] +=1
    def tick(self, global_time):
        tick_inward_flow(global_time)
    def tick_inward_flow(self, global_time):
        traffic_entrant = traffic_entrance.tick(global_time)
        if traffic_entrant != None:
            pass
        else:
            self.put_car_in(traffic_entrant)


    def tick_traffic_state(self):
        self.current_timer -=KeyConstants.TICK_RATE
        if self.current_timer < 0:
            if self.is_yellow:
                self.is_yellow = False
                self.current_timer += self.timers[self.current_state]
            else:
                if self.current_state == len(self.traffic_matrix) -1 :
                    self.current_state = 0
                else:
                    self.current_state += 1
                self.is_yellow = True
                self.current_timer += KeyConstants.YELLOW_PENALTY

    def tick_other_flow(self):
        if self.is_yellow:
            return None
        relative_flow= self.get_traffic_state(self.current_state)
        entrance_chosen = random.choices(self.entrance_names, relative_flow)
        entrance_index= self.get_name_index(entrance_chosen)
        if self.car_queue[entrance_index] > 0:
            self.car_queue[entrance_index] -=1
            return random.choices(self.entrance_names, self.get_traffic_flow(entrance_chosen))
        else:
            return None

    def tick(self, global_time):
        self.tick_traffic_state()
        self.tick_inward_flow(global_time)
        return self.tick_other_flow()

    def has_entrance(self, name):
        return name in self.entrance_name_list

