import random

class Game:
    __number = None
    __best_score = None

    def play(self):
        playing = True
        rounds = 1

        while playing:
            print("Round " + str(rounds) + ": \n")
            self.__number = random.randint(1, 100)

            attempts = 0

            won = False
            while not won:
                guess = int(input("Guess a number!: "))
                if guess == self.__number:
                    attempts += 1
                    won = True
                    print("You've guessed the number with " + str(attempts)+ " attempts!")
                elif guess > self.__number:
                    print("Lower!")
                    attempts += 1
                elif guess < self.__number:
                    print("Higher!")
                    attempts += 1

            if self.__best_score is None:
                self.__best_score = attempts
            elif self.__best_score > attempts:
                print("New low-score!")
                self.__best_score = attempts
            else:
                print("Oh no! You must do better than your best score to continue! Game over!")
                playing = False

            print("Next round!")
            rounds += 1

Game().play()