# Read an integer input 'n' which represents the number of elements in the initial set
n = int(input())

# Read 'n' space-separated integers, convert them to a set of integers 's'
s = set(map(int, input().split()))

# Read an integer 'm' which represents the number of commands to perform on the set
m = int(input())

# Loop through each command
for _ in range(m):
    # Read a command, split it into a list. For example: ["remove", "5"]
    command = input().split()
    
    # If the command is "remove", remove the specified element from the set
    # This will raise an error if the element is not present
    if command[0] == "remove":
        s.remove(int(command[1]))
    
    # If the command is "discard", remove the specified element if present
    # This will NOT raise an error if the element is not in the set
    elif command[0] == "discard":
        s.discard(int(command[1]))
    
    # If the command is "pop", remove and return an arbitrary element from the set
    elif command[0] == "pop":
        s.pop()
        
# Print the sum of all remaining elements in the set
print(sum(s))
