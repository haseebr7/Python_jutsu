class Car:
    def __init__(self,brand, color):
        self.brand = brand
        self.color = color
        self.mileage = 0
        self.engine_on = False
    def engine_start(self):
        self.engine_on = True
        print(f"The {self.color} car's engine is starting... Vrooom! 🚗💨")
    def drive(self, drive):
        if self.engine_on:
            self.mileage += drive
            print(f"You speed is {drive} km.")
        else:
            print("Engine is off, can't drive!")
    def info(self):
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")
        print(f"Mileage: {self.mileage} km")
        print(f"Engine On: {self.engine_on}")

car1 =  Car("honda", "Red")
speed = 2

while True:
    Yoo = input("info/acc(Accelerate)/start").lower()
    if Yoo == "info":
        car1.info()
    elif Yoo == "acc":
        car1.drive(speed)
        speed += 10
    elif Yoo == "start":
        car1.engine_start()
    else:
        print("Invalid command. Type: info / acc / start")
