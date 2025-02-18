tests = [
    "5424 1801 2345 6789",
    "5424 1801 2445 6789",
    "4494659074635986"
]

class VisaCard:
    __internal_card_number: str = None
    __valid_characters: [chr] = "1234567890- "

    def __init__(self, card_number: str):
        self.__internal_card_number \
            = card_number.replace('-', '').replace(' ', '')


    def valid(self) -> bool:
        for x in self.__internal_card_number:
            if x not in self.__valid_characters:
                return False

        if len(self.__internal_card_number) != 16:
            return False

        card_sum = 0
        for i in range(1, len(self.__internal_card_number), 2):
            card_sum += int(self.__internal_card_number[i])

        card_product_sum = 0
        for i in range(0, len(self.__internal_card_number), 2):
            number = int(self.__internal_card_number[i]) * 2
            output = 0
            if number >= 10:
                for c in str(number):
                    output += int(c)
            else:
                output = number
            card_product_sum += output

        if (card_sum + card_product_sum) % 10 == 0:
            return True
        else:
            return False

for card_number in range(1000000000000000, 9999999999999999, 1):
    if VisaCard(str(card_number)).valid():
        print(str(card_number) + " is valid!")





