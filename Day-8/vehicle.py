class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

vehicle = Vehicle()
vehicle.move()
car = Car()
car.move()
