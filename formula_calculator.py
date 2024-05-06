# Forumla Calculator

import math

# begins the program
choice = input("Please type start to begin the program. Type quit to end it.")
history = []

def show_history(index):
    print(history[index])

def quadratic_formula(a, b, c):
    answer_p = ((b * -1) + int(math.sqrt(int(b * b)) - 4 * a * c)) / (2 * a)
    answer_m = ((b * -1) - int(math.sqrt(int(b * b)) - 4 * a * c)) / (2 * a)
    print(answer_p)
    print(answer_m)
    history.append("quad: " + str(answer_p) + ", " + str(answer_m))

def pythagorean_theorem(a, b):
    answer = math.sqrt((a * a) + (b * b))
    print(answer)
    history.append("pyth: " + str(answer))

def circle_area(r):
    answer = math.pi * float(r) * float(r)
    print(answer)
    history.append("cirA: " + str(answer))

def circumference(d):
    answer = math.pi * float(d)
    print(answer)
    history.append("cirC: " + str(answer))

while choice != "quit":
    # chooses which function to run
    choice = input("What function would you like to run?: Quadratic Formula (quad), Pythagorean Theorem (pyth), Circle Area (cirA), Circle Circumference (cirC), View History (hist/histALL), Quit (quit)")

    if choice == "quad":
        # finds the value of x in the quadratic formula
        a = int(input("What is the value of A?"))
        b = int(input("What is the value of B?"))
        c = int(input("What is the value of C?"))
        quadratic_formula(a, b, c)

    elif choice == "pyth":
        # finds the value of c in the pythagorean theorem
        a = int(input("What is the value of A?"))
        b = int(input("What is the value of B?"))
        pythagorean_theorem(a, b)

    elif choice == "cirA":
        # finds the area of a circle
        r = input("What is the radius of the circle? (Do not included units)")
        circle_area(r)

    elif choice == "cirC":
        # finds the circumference of a circle
        d = input("What is the diameter of the circle? (Do not included units)")
        circumference(d)

    elif choice == "hist":
        # shows a specific instance (index) of a previous function that was run
        hist_number = int(input("Which instance of your history would you like to view? (first is 0, second is 1, etc.)"))
        show_history(hist_number)

    elif choice == "histALL":
        # shows every instance of previous functions that were ran
        print(history)
