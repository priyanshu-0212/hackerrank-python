if __name__ == '__main__':  
    # This checks if the script is being run directly (not imported as a module)
    
    a = int(input())  
    # Takes input from the user, converts it to an integer, and stores it in variable 'a'
    
    b = int(input())  
    # Takes another input from the user, converts it to an integer, and stores it in variable 'b'
    
    print(a//b)  
    # Performs integer (floor) division of 'a' by 'b' and prints the result (no remainder)
    
    print(a/b)  
    # Performs normal (floating-point) division of 'a' by 'b' and prints the result (can be decimal)
