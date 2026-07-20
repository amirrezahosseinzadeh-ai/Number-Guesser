import random

def validate_input(user_guess):
        if not user_guess.isdigit():
            print("Invalid input. please try again.")
            return False

        user_guess = int(user_guess)
        if user_guess > 100 or user_guess < 1:
            print("your guess is out of range. please try again. Your guess should be between 1 and 100")
            return False
        
        return True


def main():
    rand_num = random.randint(1, 100)
    score = 100

    while True:
        
        user_guess = input("Guess a number between 1 and 100: ")

        if user_guess == "q":
            print("Thank you for playing. Goodbye!")
            break

        if not validate_input(user_guess):
            continue

        user_guess = int(user_guess)
        if rand_num > user_guess:
            print("Your guess is too low, please try again!")
        elif rand_num < user_guess:
            print("Your guess is too high, please try again!")
        else:
            print("Congratulations! You guessed the correct number!")
            print(f"Your score is: {score}")
            break

        score -= 10
        score = max(score, 0)


if __name__ == "__main__":
    main()