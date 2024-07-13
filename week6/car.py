class Car: 

    def __init__(self,make,year,model):
        self.make = make
        self.year = year 
        self.model = model 
        self.odometer_reading= 0

    def get_descriptive_name(self):
        name = f"{self.year} {self.make} {self.model}"
        return name
    
    def odometer_read(self):
       print(f"this car has reading of : {self.odometer_reading}") 

    def update_odometer(self, mileage):
        if mileage>= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("bhjhjj")

mycar =  Car("toyota","2020","corolla")   
print(mycar.update_odometer(10))
print(mycar.odometer_read())
