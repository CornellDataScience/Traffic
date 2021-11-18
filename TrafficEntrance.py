""" Defines an entrance of external traffic flow into the system.
Includes the time periods for which traffic enters, the ratio of traffic entering at that given time for each entrance
As well as number representing number of cars entering per second (CPS). Also includes trackers for tick rates to release cars.
 """
import TrafficFlow

class TrafficEntrance:
    def __init__(self, traffic_flows):
        self.traffic_flows = traffic_flows

    def tick(self, global_time):
        if len(self.traffic_flows) == 0:
            return None
        if global_time < self.traffic_flows[0].start_time:
            return None
        if global_time > self.traffic_flows[0].end_time:
            self.traffic_flows.pop(0)
            self.tick(global_time)
        return self.traffic_flows[0].tick()
