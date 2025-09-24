if __name__ == '__main__':            # This block runs only if the script is executed directly
    n = int(input())                  # Read an integer n (the number of elements in the array)

    arr = map(int, input().split())   # Read n space-separated integers and convert each to int.
                                      # 'arr' is now an iterator of integers.

    unique_scores = list(set(arr))    # Convert arr to a set to remove duplicate values,
                                      # then convert it back to a list.

    unique_scores.sort()              # Sort the list in ascending order.

    print(unique_scores[-2])          # Print the second largest number:
                                      # -1 is the last element (max), -2 is the second last element.
