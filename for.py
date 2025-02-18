
number = 0
for i in range(int(input("pick a number: ")) + 1):
    number += i

print(number)

if number >= 1000:
    print("Wow thats a big number!")
