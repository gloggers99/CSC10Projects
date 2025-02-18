list = ["one", "two", "three", "four"]
query = input("What item are you looking for? ")

if query in list:
    for i in range(len(list)):
        if list[i] == query:
            print("Item found, index=" + str(i))

else:
    print("That isn't in the list!")