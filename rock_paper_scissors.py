import random
from operator import index

# the value is the choice which the key beats
choices = {
    "rock": 2,    # 0
    "paper": 0,   # 1
    "scissors": 1 # 2
}

class Game:
    __user_score = 0
    __computer_score = 0

    def play_round(self):
        print("score: user: " + str(self.__user_score) + " computer: " + str(self.__computer_score))
        user_choice = input("rock, paper, scissors?: ")
        computer_choice = str(random.choice(list(choices)))

        print("Computer plays " + computer_choice + "!")

        if user_choice == computer_choice:
            print("Tie! No point!")
        elif choices[user_choice] == index(choices[user_choice]):
            print("Round won! One point to you!")
            self.__user_score += 1
        else:
            print("Round lost. Point to computer!")
            self.__computer_score += 1

        if self.__user_score == 3:
            print("You win! Game over.")
            exit(0)
        elif self.__computer_score == 3:
            print("Computer wins! Game over.")
            exit(0)

game = Game()
while True:
    game.play_round()
