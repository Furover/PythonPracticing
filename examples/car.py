class SmallCar:
    def __init__(self,brand,color,motor,speed = 0,state = False):
        self.brand = brand
        self.color = color
        self.motor = motor
        self.speed = speed
        self.state = state

    def ChangeState(self):
        self.state = True
        print("Car is turned", "on" if self.state else "off")

    def Accelerate(self):
        if self.state and self.speed < 200:
            print("Current speed: ", self.speed)
            print("Accelerating...")
            self.speed += 10
            print("Current speed: ", self.speed)
        else:
            print("Cannot accelerate, check if car is turned on or at it's speed limit!")

    def Stop(self):
        if self.state and self.speed >= 10:
            print("Current speed: ", self.speed)
            while self.speed != 0:
                print("Stopping...")
                self.speed -= 10
                print("Current speed: ", self.speed)
            print("Car is now stopped")
        else:
            print("Cannot stop, check if car is turned on or stopped!")

    def Deaccelerate(self):
        if self.state and self.speed >= 10:
            print("Current speed: ", self.speed)
            print("Deaccelerating...")
            self.speed -= 10
            print("Current speed: ", self.speed)
        else:
            print("Cannot deaccelerate, check if car is turned on or stopped!")
        

class MotorBike:
    def __init__(self,brand,color,cylinderCapacity,speed = 0,state = False):
        self.brand = brand
        self.color = color
        self.cylinderCapacity = cylinderCapacity
        self.speed = speed
        self.state = state

class LargeCar:
    def __init__(self,brand,color,motor,axis,speed = 0,state = False):
        self.brand = brand
        self.color = color
        self.motor = motor
        self.speed = speed
        self.state = state
        self.axis = axis