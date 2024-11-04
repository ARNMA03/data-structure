class PublicUtilityVehicle:
    def __init__(self):
        self.puv_rates = {
            "bus": [12, 10, 9.50],
            "jeepney": [12, 10, 9.50],
            "tricycle": [50, 40, 38]
        }

    def show_fare(self, vehicle):
        if vehicle == "a":
            self.print_fare("bus")
        elif vehicle == "b":
            self.print_fare("jeepney")
        elif vehicle == "c":
            self.print_fare("tricycle")
        else:
            print("\t\tInvalid input.")

    def print_fare(self, vehicle_type):
        fares = self.puv_rates[vehicle_type]
        print(f"""
    For regular: ₱{fares[0]:.2f}
    For student: ₱{fares[1]:.2f}
    For senior: ₱{fares[2]:.2f}""")

    def run(self):
        vehicle = display()
        self.show_fare(vehicle)

def display():
    user = input("""
    a. Bus
    b. Jeepney
    c. Tricycle

    Enter PUV (public utility vehicle): """).lower()
    return user


# Instantiate and run the program
puv = PublicUtilityVehicle()
puv.run()
