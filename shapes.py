import math

run = True

while run:
    match input("What shape would you like to print (christmas tree/diamond/hourglass/circle)"):
        case "christmas tree":
            for i in range(1, 21, 2):
                print(("*"*i).center(20))
            for i in range(1, 4):
                print(("*"*4).center(20))

        case "diamond":
            for i in range(1, 21, 2):
                print(("*" * i).center(22))
            for i in range(21, 1, -2):
                print(("*" * i).center(22))
        case "hourglass":
            for i in range(21, 1, -2):
                print(("*" * i).center(22))
            for i in range(1, 21, 2):
                print(("*" * i).center(22))
        case "circle":
            for i in range(-100, 100, 10):
                print(("*" * (math.cos(math.radians(i)) * 69).__round__()).center(101))
        case _:
            print("Invalid input!")