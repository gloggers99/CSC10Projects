def is_cyclops_number(number) -> bool:
    number = bin(number).replace("0b", "")
    if len(str(number)) % 2 == 0:
        return False
    if str(number).count('0') > 1:
        return False
    if str(number).count('1') % 2 != 0:
        return False

    left = True
    left_count = 0
    right_count = 0
    for c in str(number):
        if c == "1":
            if left:
                left_count += 1
            else:
                right_count += 1
        if c == "0":
            left = False

    if left_count != right_count:
        return False
    return True




test_numbers = range(0, 1000)
print("{:>10}  {:^30}  {}".format("number", "binary", "cyclops"))
print("-"*50)
for number in test_numbers:
    if is_cyclops_number(number):
        print("{:>10}   | {:^25} |   {}".format(str(number), str(bin(number)).replace("0b", ''), is_cyclops_number(number)))

