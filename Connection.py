class Connection:
    def __init__(self, speed_limit, length_miles, entrance_name, exit_name, cars_on_road):
        self.speed_limit = speed_limit
        self.length_miles = length_miles
        self.entrance_name = entrance_name
        self.exit_name = exit_name
        self.cars_on_road = cars_on_road
        if not self.checkInvariants(self):
            raise TypeError("Invalid constructor for Connection")
    def checkInvariants(self):
        for car in self.cars_on_road:
            if car < 0 or car > self.length_miles:
                return False
        return True
