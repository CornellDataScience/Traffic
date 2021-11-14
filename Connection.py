class Connection:
    def __init__(self, speed_limit, length_miles, entrance_name, exit_name):
        self.speed_limit = speed_limit
        self.length_miles = length_miles
        self.entrance_name = entrance_name
        self.exit_name = exit_name
        if not self.checkInvariants(self):
            raise TypeError("Invalid constructor for Connection")
    def checkInvariants(self):
        return True
    def get_wait_time(self):
        self.length_miles / self. speed_limit * 3600

