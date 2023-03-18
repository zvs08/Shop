from Rental import WaterVehicleRental, Customer

def main():
    shop = WaterVehicleRental([10, 10, 10])
    customer = Customer()

    while True:
        print("""
        ====== Water Sport Rental =======
        1. Display available vehicles
        2. Request a boat on hourly basis $25
        3. Request a canoe on hourly basis $15
        4. Request a paddleboard on hourly basis $10
        5. Return all water vehicles
        6. Exit
        """)

        choice = input("Enter choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue

        if choice == 1:
            shop.displaystock()

        elif choice >= 2 and choice <= 4:
            type = sorted(list(shop.stock.keys()))[choice - 2]
            customer.rentalTime[type] = shop.rent_water_vehicle(type, customer.request_water_vehicle(type))

        elif choice == 5:
            customer.bill = shop.return_water_vehicle(customer.return_all())
            customer.rentalTime, customer.vehicles = {},{}        
        elif choice == 6:
            break
        else:
            print("Invalid input. Please enter number between 1-6 ")        
    print("Thank you for using the boat rental system.")



if __name__=="__main__":
    main()