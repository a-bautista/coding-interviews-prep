'''
    Given an array of integers sorted in increasing order and a target, find the index of the first element in the array that is 
    larger than or equal to the target. Assume that it is guaranteed to find a satisfying number.

    Input:

    arr = [1, 3, 3, 5, 8, 8, 10]
    target = 2
    Output: 1

    Explanation: the first element larger than 2 is 3 which has index 1.

    Input:

    arr = [2, 3, 5, 7, 11, 13, 17, 19]
    target = 6
    Output: 3
'''

'''
    arr = [1, 3, 3, 5, 8, 8, 10]
    target = 2

    [1, 3, 3, 5, 8, 8, 10]
     0  1  2  3  4  5  6
     ^                 ^

     mid = left + (right - left)//2
     mid = 3

     5 >= 2 yes but is this the first number that is greater than 2? We don't know. Discard the right side
     right = mid-1 # 2
     mid = 0 + (2-0)//2 = 1

    boundary_index = mid
    left = 0
    mid = 1
    right = 2

    3>=2 yes, but is this the first number that is greater than 2? We don't know. Continue discarding the right side.
    right = mid -1 # 0
    left = 0

    if I want to end the loop, I need to change the while loop to left < right

'''

from typing import List

def first_not_smaller(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr)-1
    first_occurrence = 0
    
    while left <= right:
        mid = left + (right - left)//2
        
        if arr[mid] >= target:
            first_occurrence = mid
            # discard the right side
            right = mid -1
        else:
            # discard the left side
            left = mid + 1
        
    return first_occurrence

def main():
    test_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_2 = [1, 3, 3, 5, 8, 8, 10]
    target_1 = 10
    target_2 = 2
    res = first_not_smaller(test_2, target_2)
    print(res)

main()