class Car:
    def __init__(self,make, model, year, ):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Car Deatils: {self.year} {self.model} {self.make}")
my_car = Car ("Ford" , "Mustang" , "2020")
my_car.display_info()