import random

start = input("Enter the start of the range: ")

while type(start) != int:
    try:
        start = int(start)
    except ValueError:
        print("Please enter a valid number.")
        start = input("Enter the start of the range: ")

end = input("Enter the end of the range: ")

while type(end) != int:
    try:
        end = int(end)
        if start > end:
            print("Please enter a valid number.")
            end = input("Enter the end of the range: ")
    except ValueError:
        print("Please enter a valid number.")
        end = input("Enter the end of the range: ")


random_number = random.randint(start, end)

guess = input("Guess a number: ")
while type(guess) != int and guess != random_number:
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        guess = input("Guess a number: ")

guess_count = 1

while guess != random_number:
    guess_count += 1
    try:
        guess = int(input("Guess a number: "))
    except ValueError:
        print("Please enter a valid number.")
        guess = input("Guess a number: ")

if guess_count == 1:
    print(f"You guessed the number in {guess_count} attempt")
else:
    print(f"You guessed the number in {guess_count} attempts")