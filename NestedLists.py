if __name__ == '__main__':                          # Run this block only if the script is executed directly
    students = []                                   # Create an empty list to hold [name, score] for each student
    
    for _ in range(int(input())):                   # Loop n times (read n from input) – one iteration per student
        name = input()                              # Read the student's name
        score = float(input())                      # Read the student's score and convert it to a float
        students.append([name, score])              # Add [name, score] as a nested list inside 'students'
    
    # Build a set of all scores (to remove duplicates), then sort it into ascending order
    scores = sorted({s[1] for s in students})       # s[1] is the score from each [name, score]
    
    second_lowest = scores[1]                       # Take the second element in the sorted unique scores → second lowest score
    
    # Collect the names of all students whose score equals the second lowest
    names = [s[0] for s in students if s[1] == second_lowest]  # s[0] is the name, s[1] is the score
    
    # Sort the names alphabetically and print each on a new line
    for name in sorted(names):
        print(name)
