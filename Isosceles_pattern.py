# Ask the user for the height of the triangle
n = int(input("Enter height: "))

# Outer loop – controls the number of rows (1 to n)
for i in range(1, n + 1):
    # Inner loop – prints stars in each row.
    # On row i, we print i stars.
    for j in range(i):
        print('*', end='')   # print a star without a newline
    print()                  # after finishing one row, move to the next line
