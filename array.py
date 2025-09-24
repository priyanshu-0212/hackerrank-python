"""This is my personal array solution which i had studied by own go through once if you want to learn in an easy manner just read the comments for getting what is going inside the code (Happy Coding 😊)  """
arr = [10, 2, 33, 24, 5, -3]
print(arr[2])
arr[2] = 3
print("This is array:", arr)

#append in array
value = int(input("Enter Input in array: "))
arr.append(value) #append means added at the last of the array
print("This is updated array after append:", arr)

#insert in array
arr.insert(3, 5)
print("This is the updated array after at a random index: ",arr)


#delete element from the last
arr.pop()
print(arr)

#remove element according to the value
arr.remove(2)
print(arr)

#slicing in array
print("This is the reverse form of array: ",arr[::-1]) #reversing the array by slicing
print(arr[1:5])#limits in slicing
print(arr[-3:])#negative slicing


#if we want to find that this element does exist in the array or not so we can use if else like
i = int(input())
if i in arr:
    print(i, "is in Array")
else:
    print("Error")


# #minimum value in the array
print(min(arr))#minimum element in array
#
# #maximum value in the array
print(max(arr))
#
# #sum of all elements in the array
print(sum(arr))
#
# #length of the array
print(len(arr))
#
# #sorting an aray
arr.sort()
print("Sorted array: ",arr)
#
# #sorting in array in reverse form
arr.sort(reverse=True)
print("Reverse Sorted array:", arr)

# making copy of an array
arr1 = arr.copy() #make a copy of an array by making a heap memory in RAM
arr1.append(77)
print("This is a copy of array: ",arr1)
