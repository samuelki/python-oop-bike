class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles =  0
    def displayInfo(self):
        print("price:", self.price)
        print("maximum speed:", self.max_speed)
        print("total miles:", self.miles)
    def ride(self):
        print("Riding")
        self.miles += 10
        return self
    def reverse(self):
        print("Reversing")
        self.miles -= 5
        # prevent having negative miles
        if self.miles < 0:
            self.miles = 0
        return self
    
bike1 = Bike(200, "25mph")
bike2 = Bike(300, "30mph")
bike3 = Bike(400, "35mph")

bike1.ride().ride().ride().reverse().displayInfo()

bike2.ride().ride().reverse().reverse().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()