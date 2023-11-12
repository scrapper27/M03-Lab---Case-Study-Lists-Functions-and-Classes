#Owen Stackhouse

#M03 Lab.py

#You provide the program with information about your car, such as the year, model, make, doors, and roof.
#It will take all that information together and generate a list for you.

#Year represents the manufacturing year of the car. Make represents the make or brand of the car.
# Model represents the model of the car. Doors represents the number of doors in the car. Roof represents the type of roof the car has (solid or sunroof). 

class Vehicle:
    def __init__(self):
        self.vehicle_type = ""

class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = ""
        self.make = ""
        self.model = ""
        self.doors = ""
        self.roof = ""

    def input_data(self):
        self.vehicle_type = "car"
        self.year = input("Enter the year: ")
        self.make = input("Enter the make: ")
        self.model = input("Enter the model: ")
        self.doors = input("Enter the number of doors (2 or 4): ")
        self.roof = input("Enter the type of roof (solid or sun roof): ")

    def display_data(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)


car = Automobile()

car.input_data()

car.display_data()