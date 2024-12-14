def main():
    # Ask the user to enter a number and initialize curr_value with it
    curr_value = int(input("Enter a number: "))

    # Use a while loop to keep doubling until curr_value is 100 or more
    while curr_value < 100:
        curr_value *= 2
        print(curr_value, end=" ")

# This line is required to call the main() function
if __name__ == '__main__':
    main()
