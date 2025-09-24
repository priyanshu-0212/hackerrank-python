# This line checks if the current script is being run directly
# and not being imported as a module in another script
if __name__ == '__main__':
    # Take input from the user and convert it to an integer
    n = int(input())

# Loop from 1 to n (inclusive)
for i in range(1, n+1):
    # Print the current value of i without moving to a new line
    # end="" ensures that all numbers are printed on the same line
    print(i, end="")
