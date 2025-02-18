my_dataset = {
    "dog": 10,
    "cat": 5,
    "zebra": 2,
    "bird": 7
}

def horiz(dataset):
    for item, amount in dataset.items():
        print(item.rjust(10) + ":" + "*"*amount)

def vert(dataset):
    # get highest amount possible out of all dict values
    largest = 0
    for item, amount in dataset.items():
        if amount > largest:
            largest = amount

    for i in range(largest, 0, -1):
        for amount in dataset.values():
            if amount < i:
                print("   ", end='')
            else:
                print(" * ", end='')
        print()
    print('-'*len(dataset)*3)

    largest_name = 0
    for item in dataset.keys():
        if len(item) > largest_name:
            largest_name = len(item)

    for i in range(0, largest_name):
        for item in dataset.keys():
            if i >= len(item):
                print("   ", end='')
            else:
                print(' ' + item[i] + ' ', end='')
        print()

print(str(my_dataset) + "\n")
horiz(my_dataset)
print()
vert(my_dataset)