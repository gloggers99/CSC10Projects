
x = int(input("enter a number"))

divisible_by = []

for i in range(x+1):
    if x % (i+1) == 0:
        divisible_by.append(i+1)

if len(divisible_by) == 2:
    print("That number is prime!")
else:
    print("Divisible by: " + str(divisible_by))