# phone number validator

class PhoneNumber:
    __internal_format: str = None

    __valid_characters: [chr] = "1234567890()- "

    def __init__(self, phone_number: str):
        for c in phone_number:
            if c not in self.__valid_characters:
                print("Invalid character in phone number!")
                exit(1)

        self.__internal_format \
            = (phone_number.replace(' ', '')
                           .replace('(', '')
                           .replace(')', '')
                           .replace('-', ''))

        if len(self.__internal_format) != 10:
            print("Phone number should only have 10 numbers.")
            exit(1)

    def __str__(self):
        return "({}) {}-{}".format(
            self.__internal_format[0:3],
            self.__internal_format[3:6],
            self.__internal_format[6:11])

print(PhoneNumber(input("Enter a phone number: ")))

