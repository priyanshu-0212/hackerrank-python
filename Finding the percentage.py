if __name__ == '__main__':
    n = int(input())                             # number of students
    student_marks = {}                           # dictionary to store name -> scores list

    for _ in range(n):
        name, *line = input().split()            # first value = name, remaining = scores
        scores = list(map(float, line))          # convert scores to floats
        student_marks[name] = scores             # store in dictionary

    query_name = input()                         # name whose average marks you want

    # compute average of that student's scores
    average = sum(student_marks[query_name]) / len(student_marks[query_name])

    # print average rounded to 2 decimal places
    print(f"{average:.2f}")
