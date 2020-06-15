def linear_search(arr, target):
    # Your code here
    for i in range(0,len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    #Compare the item in the middle of the data set to the item we are searching for
    arr[len(arr)//2]
    #   If it is the same, stop. We found it and are done!
    #   Else, if the item we are searching for is LESS than the item in the middle:
    #       Eliminate the RHS of list. Repeat step 1 with only the LHS of list.
    #   Else, the item we are searching for is GREATER than the item in the middle:
    #       Eliminate the LHS of list. Repeat step 1 with only the RHS of the list.

    return -1  # not found
