user_choice = int(input("Choose a big number: "))

for i in range(user_choice):
    total = 0
    for j in range(i + 1):
        total += j
        if total >= user_choice:
            print(j)
            exit()