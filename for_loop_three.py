user_input = int(input("Pick a number: "))
pattern_one = 0
pattern_two = 2
for i in range(user_input + 1):
    print(str(i) + " " + str(user_input - i) + " " + str(pattern_one) + " " + str(pattern_two))
    pattern_one += 3
    pattern_two += 3
