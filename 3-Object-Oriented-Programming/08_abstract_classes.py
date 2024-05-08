import random


# Create an abstract class
class AbstractGame:
    def start(self):
        while True:
            start = input("Would you like to play?")
            if start.lower() == "yes":
                break

        self.play()

    def end(self):
        print("The game has ended.")
        self.reset()

    # abstract methods
    def play(self):
        raise NotImplementedError("You must provide an implementation for play()")

    def reset(self):
        raise NotImplementedError("You must provide an implementation for reset()")


class RandomGuesser(AbstractGame):
    def __init__(self, rounds):
        self.rounds = rounds
        self.round = 0

    def reset(self):
        self.round = 0

    def play(self):
        while self.round < self.rounds:
            self.round += 1

            print(f"Welcome to round {self.round}. Let's begin!")
            random_num = random.randint(0, 10)
            while True:
                guess = input("Enter a number between 1-10: ")
                if int(guess) == random_num:
                    print("You got it!")
                    break
        self.end()


class AnotherGame(AbstractGame):
    pass


game = RandomGuesser(2)
game.start()  # the game starts

game = AnotherGame()
game.start()  # NotImplementedError: You must provide an implementation for play()

'''
Abstract Animal Class

Create an abstract "Animal" class that contains the following methods.
    - "sleep()", a concrete method that outputs "ZzzZzz" to the console.
    - "animal_sound()", an abstract method that raises a "NotImplementedError" if called.
    - "wake_up()", a concrete method that calls "animal_sound()" and outputs "I am awake!" to the console.

After creating the "Animal" class, create a subclass named "Lion" that implements the "Animal" class. When 
"animal_sound()" is called on an instance of the "Lion" class it should output "Roar!"
'''


class Animal:
    def sleep(self):
        print("ZzzZzz")

    def animal_sound(self):
        raise NotImplementedError("You must provide an implementation for animal_sound()")

    def wake_up(self):
        self.animal_sound()
        print("I am awake!")


class Lion(Animal):
    def animal_sound(self):
        print("Roar!")