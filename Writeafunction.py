def is_leap(year):                 # Define a function named 'is_leap' that takes 'year' as input
    leap = False                   # Initially assume the year is not a leap year (set leap to False)

    # Check leap year conditions:
    # A year is a leap year if:
    #   - it is divisible by 400 OR
    #   - it is divisible by 4 but NOT divisible by 100
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        leap = True                # If the above condition is true, mark it as a leap year (True)

    return leap                    # Return True if leap year, otherwise False

year = int(input())                # Take input from user, convert it to integer, and store in 'year'
print(is_leap(year))               # Call the 'is_leap' function with input year and print the result
