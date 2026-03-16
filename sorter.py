from constants import *

def is_bulky(length, width, height):
    # bulky if any dimension is >= 150
    if length >= 150 or width >= 150 or height >= 150:
        return True
    # or total is >= 10^6 cm^3
    elif length * width * height >= 10**6:
        return True

    return False

def is_heavy(mass):
    # heavy if mass is >= 20 kg
    if mass >= 20:
        return True

    return False

def get_input(user_input):
    while True:
        if user_input == MASS:
            result = float(input(f'Please enter the {user_input} of the package in kg: '))
        else:
            result = float(input(f'Please enter the {user_input} of the package in cm: '))
        # validate  input must be > 0
        if result > 0:
            break
        else:
            print(f'Invalid input. Please enter a positive value for {user_input}.')

    return result


def sort(length, width, height, mass):
    # rejected if bulky and heavy
    if is_bulky(length, width, height) and is_heavy(mass):
        return REJECTED
    # special if bulky or heavy
    elif is_bulky(length, width, height) or is_heavy(mass):
        return SPECIAL
    # otherwise is standard
    else:
        return STANDARD

def sorter():
    print("Welcome to the Bulky package sorter!")
    length = get_input(LENGTH)
    width = get_input(WIDTH)
    height = get_input(HEIGHT)
    mass = get_input(MASS)

    # get the result
    result = sort(length, width, height, mass)
    print("The package is sorted as:", result)
    return result
