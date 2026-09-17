class Vehicle:

    def __init__(self, wheels, persons):
        if self.__class__ == Vehicle:
            raise TypeError("Object of Vehicle class cannot be created")

        self.wheels = wheels
        self.persons = persons

    def calculate_toll(self):
        pass


class TwoWheeler(Vehicle):

    def calculate_toll(self):
        toll = 20

        if self.persons > 2:
            toll = toll + (self.persons - 2) * 10

        return toll


class ThreeWheeler(Vehicle):

    def calculate_toll(self):
        toll = 30

        if self.persons > 3:
            toll = toll + (self.persons - 3) * 20

        return toll


class FourWheeler(Vehicle):

    def calculate_toll(self):
        toll = 40

        if self.persons > 4:
            toll = toll + (self.persons - 4) * 40

        return toll


class HeavyVehicle(Vehicle):

    def calculate_toll(self):
        toll = 60

        if self.persons > 6:
            toll = toll + (self.persons - 6) * 100

        return toll

while True:

    print("\n----- TOLL MENU -----")
    print("1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Thank you!")
        break

    persons = int(input("Enter number of persons: "))

    if choice == 1:
        vehicle = TwoWheeler(2, persons)

    elif choice == 2:
        vehicle = ThreeWheeler(3, persons)

    elif choice == 3:
        vehicle = FourWheeler(4, persons)

    elif choice == 4:
        wheels = int(input("Enter number of wheels: "))

        if wheels <= 4:
            print("Heavy vehicle must have more than 4 wheels")
            continue

        vehicle = HeavyVehicle(wheels, persons)

    else:
        print("Invalid choice")
        continue

    print("Total Toll = Rs.", vehicle.calculate_toll())
