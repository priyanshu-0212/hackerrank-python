import math   # Imports the math module (not actually used in this code)
import os     # Imports the os module (not used here)
import random # Imports the random module (not used here)
import re     # Imports the regular expressions module (not used here)
import sys    # Imports the sys module (not used here)

# Main entry point of the program
if __name__ == '__main__':
    n = int(input().strip())  
    # Reads input from the user as a string, removes leading/trailing whitespace,
    # converts it to an integer, and stores it in variable n

# Checks if n is odd
if (n % 2 != 0):
    print("Weird")  
    # If n is odd, prints "Weird"

# Checks if n is even and between 2 and 5 (inclusive)
elif (n % 2 == 0 and 2 <= n <= 5):
    print("Not Weird")  
    # If n is even and in the range 2–5, prints "Not Weird"

# Checks if n is even and between 6 and 20 (inclusive)
elif (n % 2 == 0 and 6 <= n <= 20):
    print("Weird")  
    # If n is even and in the range 6–20, prints "Weird"

# Checks if n is even and greater than 20
elif (n % 2 == 0 and n > 20):
    print("Not Weird")  
    # If n is even and greater than 20, prints "Not Weird"
