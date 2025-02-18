word = input("Enter a word: ")

for i in range(0, len(word), 2):
    print(word[i])

print()

for i in range(1, len(word), 2):
    print(word[i])

number = input("Enter a big number: ")

print()

output = 0
for i in range(0, len(number), 3):
    print(number[i])
    output += int(number[i])

print(output)

print()

output = 0
number = input("Enter a number: ")
number = int(number) * int(number)
if number >= 10:
    number = str(number)
    for c in number:
        output += int(c)
else:
    output = number

print(output)