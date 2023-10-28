"""CP1404 Week 06 practice and extension
Driving Simulator"""

from car import Car

MENU = "d) drive\nr) refuel\nc) change vehicle\nq) quit"


def main():
    print("Let's drive!")
    your_car = Car(input("Enter your car name: "), 100)
    print(MENU)
    display_car_status(your_car)
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice == "d":
            drive_car(your_car)
        elif choice == "r":
            refuel_car(your_car)
        elif choice == "c":
            your_car = Car(input("Enter new car name: "), your_car.fuel)
        else:
            print("Invalid choice")
        print(MENU)
        display_car_status(your_car)
        choice = input("Enter your choice: ").lower()
    print(f"Good bye {your_car}'s driver.")


def drive_car(car):
    distance_to_drive = get_valid_number(0, "How many km do you wish to drive?", "Distance")
    distance_travelled = car.drive(distance_to_drive)
    if distance_travelled < distance_to_drive:
        fuel_warning = " and ran out of fuel."
    else:
        fuel_warning = "."
    print(f"The car drove {distance_travelled}km{fuel_warning}")


def get_valid_number(minimum, prompt, type):
    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input(prompt))
            if number > minimum:
                is_valid_number = True
            else:
                print(f"{type} must be >= 0")
        except ValueError:
            print("Invalid number")
    return number  # error checking ensures variable is defined


def refuel_car(your_car):
    amount_of_fuel = get_valid_number(0, "How much fuel do you want to add? ", "Fuel units")
    your_car.fuel += amount_of_fuel


def display_car_status(your_car):
    print(f"{your_car.name}, fuel={your_car.fuel}, odo={your_car._odometer}")


main()
