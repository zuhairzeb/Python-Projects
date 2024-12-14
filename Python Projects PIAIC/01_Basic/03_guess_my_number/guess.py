import random

def main():
    # Generate the secret number at random!
    secret_number = random.randint(1, 99)  # Random number between 1 and 99
    
    print("I am thinking of a number between 1 and 99...")
    
    # Get the first guess from the user
    guess = int(input("Enter a guess: "))
    
    # Keep prompting the user until the correct number is guessed
    while guess != secret_number:
        if guess < secret_number:  # Guess is too low
            print("Your guess is too low")
        else:  # Guess is too high
            print("Your guess is too high")
        
        # Prompt for a new guess
        guess = int(input("Enter a new guess: "))
    
    # If the user guesses correctly
    print(f"Congrats! The number was: {secret_number}")
    

if __name__ == '__main__':
    main()
