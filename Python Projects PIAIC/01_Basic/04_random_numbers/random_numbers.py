import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    prints 10 random numbers in the range 1 to 100.
    Each time the program runs, it generates different numbers.
    """
    # Generate and print 10 random numbers
    for _ in range(N_NUMBERS):
        random_number = random.randint(MIN_VALUE, MAX_VALUE)
        print(random_number)

if __name__ == '__main__':
    main()
