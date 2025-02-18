password = "stargaard"

attempts = 10
for attempt in range(attempts, 0, -1):
    if input("enter a password: ") == password:
        print("wow! good job!")
        exit(0)
    else:
        print("Nope!")
        print("Attempts left: " + str(attempt-1))

print("out of attempts!")