import datetime

class WaterVehicleRental:
    
    def __init__(self,stock=[0, 0, 0]):
        """
        Our constructor class that instantiates bike rental shop.
        """
        self.stock = {}
        self.prices = {"Boat":25, "Canoe":15, "Paddleboard":10}
        types = ["Boat", "Canoe",  "Paddleboard"]
        for l in range(0, len(types)):
            self.stock[types[l]] = stock[l]

    def displaystock(self):
        """
        Displays the number of each type of the vehicles currently available for rent in the shop.
        """
        for b in self.stock:
            print("We have currently {} {}s available to rent.".format(self.stock[b], b))
        return self.stock

    def rent_water_vehicle(self, type, n):
        """
        Rents a bike on hourly basis to a customer.
        """
        if n <= 0:
            print("Number should be positive!")
            return None
        
        elif n > self.stock[type]:
            print("Sorry! We have currently {} {}(s) available to rent.".format(self.stock[type], type))
            return None
        
        else:
            now = datetime.datetime.now()                      
            print("You have rented a {} {}(s) today at {}".format(n,type, now))
            print("Have a fun water trip!")

            self.stock[type] -= n
            return now      
    
    def return_water_vehicle(self, return_request):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
        rentalTimes = return_request[0]
        items = return_request[1]
        bill = 0
        
        for v in items:
            if not items[v]:
                continue
            self.stock[v] += items[v]
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTimes[v]
            
            s = max(1, round(rentalPeriod.seconds / 3600)) * self.prices[v] * items[v]
            
               
            if (3 <= items[v] <= 5):
                print("You are eligible for Family rental promotion of 20% discount for {} price".format(v))
                s = s * 0.8
            bill += s
        
        if bill:
            print("Thanks for returning the vehicles. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill
        else:
            print("Are you sure you rented something with us?")
            return None



class Customer:

    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """
        
        self.vehicles = {}
        self.rentalTime = {}
        for l in ["Boat", "Canoe",  "Paddleboard"]:
            self.vehicles[l] = 0
            self.rentalTime[l] = 0
        self.bill = 0

    
    def request_water_vehicle(self, type):
        """
        Takes a request from the customer for the number of bikes.
        """
                      
        n = input("How many items would you like to rent? ")
        try:
            n = int(n)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if n < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.vehicles[type] += n
        return n
     
    def return_all(self):
        """
        Allows customers to return all the rented vehicles to the shop.
        """
        r = 0
        for q in self.vehicles.values():
            r += q
        if self.rentalTime and r:
            return [self.rentalTime, self.vehicles]  
        else:
            return [0,{}]