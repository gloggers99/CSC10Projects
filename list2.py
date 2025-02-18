class ManagedList:
    __list: [str] = []

    def get_index_of(self, string) -> int:
        if string in self.__list:
            for i in range(len(self.__list)):
                if self.__list[i] == string:
                    return i
        else:
            return -1

    def add(self, string):
        self.__list.append(string)

    def insert(self, string_before, string):
        index = self.get_index_of(string_before)
        if index == -1:
            print("That string doesn't exist!")
        else:
            self.__list.insert(index, string)

    def remove(self, string):
        if string in self.__list:
            self.__list.remove(string)
        else:
            print("Doesn't exist!")

    def count(self, string) -> int:
        return self.__list.count(string)

    def replace(self, string_to_replace, new_string):
        self.__list[self.get_index_of(string_to_replace)] = new_string

    def print(self):
        print(self.__list)

my_list = ManagedList()

run = True
while run:
    my_list.print()
    match input("How would you like to modify your list? (add/insert/remove/count/replace/quit)"):
        case "add":
            my_list.add(input("What would you like to add?: "))
        case "insert":
            my_list.insert(input("What would you like to insert after?: "), input("With what?: "))
        case "remove":
            my_list.remove(input("What would you like to remove?: "))
        case "count":
            print(my_list.count(input("What element would you like to count?: ")))
        case "replace":
            my_list.replace(input("What would you like to replace?: "), input("With what?:"))
        case "quit":
            run = False
        case _:
            print("Invalid option!")
