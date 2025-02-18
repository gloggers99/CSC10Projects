input_string = "bump ow fun waps wept guy".replace(' ', '')
input_string_hex = input_string.encode("utf-8").hex()

every_fourth = ""
for i in range(len(input_string_hex)-1, 0, -4):
    every_fourth += input_string_hex[i]

every_fourth = every_fourth[::-1]

final_string = ""
for i in range(0, len(every_fourth), 2):
    final_string += chr(int(every_fourth[i:i+2], 16))

print(final_string)