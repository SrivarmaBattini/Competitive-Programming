class RideSharingSystem:

    def __init__(self):
        self.rider = []
        self.driver = []
        self.rider_idx = 0
        self.driver_idx = 0

    def addRider(self, riderId: int) -> None:
        self.rider.append(riderId)

    def addDriver(self, driverId: int) -> None:
        self.driver.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        
        if self.rider_idx >= len(self.rider) or self.driver_idx >= len(self.driver):
            return [-1, -1]

        rider_id = self.rider[self.rider_idx]
        driver_id = self.driver[self.driver_idx]

        self.rider_idx += 1
        self.driver_idx += 1

        return [driver_id, rider_id]

    def cancelRider(self, riderId: int) -> None:
        for i in range(self.rider_idx, len(self.rider)):
            if self.rider[i] == riderId:
                self.rider.pop(i)
                return


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)