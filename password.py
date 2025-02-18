# Lucas Marta

class Program:
    __attempts = 3
    __password = "password123"

    def authenticate(self):
        while self.__attempts > 0:
            guess = input("Enter password: ")

            if guess == self.__password:
                print("You entered the correct password!")
                self.__attempts -= 1
                break
            else:
                if self.__attempts == 1:
                    print("Wrong password you are out of attempts! Sorry!")
                    exit(1)
                else:
                    print("Wrong password! " + str(self.__attempts - 1) + " attempts left!")
                    self.__attempts -= 1

Program().authenticate()