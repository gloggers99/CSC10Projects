user_input = input("Enter your name (or quit): ")
if user_input == "quit":
    exit(0)
letter_choice = input("Enter a letter")

count = 0

for c in user_input:
    print(c)
    if c == letter_choice:
        count += 1

print("\n" + letter_choice + " occurs " + str(count) + " times.")
