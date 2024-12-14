def main():
    # Ask the user for an initial number
    curr_value = int(input("Enter a number: "))
    
    # Repeat doubling and printing the value while it's less than 100
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")
    
    print()  # To ensure a clean ending line after the output


if __name__ == '__main__':
    main()
