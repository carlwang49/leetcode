"""
Date: 2023-10-26
Author: Carl Wang
Purpose: Implement Binary Search
"""

def binary_search_1(sorted_array: list, left: int, right: int, x: int):
    """
    binary search in recursive
    """

    if left > right:
        return -1

    mid = (left + right) // 2

    if x == sorted_array[mid]:
        return mid
    elif x < sorted_array[mid]:
        return binary_search_1(sorted_array, left, mid-1, x)
    else:
        return binary_search_1(sorted_array, mid+1, right, x)
    

def binary_search_2(sorted_array: list, x: int):
    """
    binary search in while loop
    """

    left = 0
    right = len(sorted_array) - 1
    
    while left <= right:
        mid = (left + right) // 2 
        if x == sorted_array[mid]:
            return mid
        elif x < sorted_array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return - 1

sorted_array = [2, 5, 6, 8, 9, 10]
print(binary_search_1(sorted_array, 0, len(sorted_array)-1, 9))
print(binary_search_2(sorted_array, 9))
    
    