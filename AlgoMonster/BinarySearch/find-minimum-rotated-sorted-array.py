'''
    A sorted array of unique integers was rotated at an unknown pivot. 
    For example, [10, 20, 30, 40, 50] becomes [30, 40, 50, 10, 20]. 
    Find the index of the minimum element in this array. 
    All the numbers are unique.

    Input: [30, 40, 50, 10, 20]

    Output: 3

    Explanation: the smallest element is 10 and its index is 3.

    Input: [3, 5, 7, 11, 13, 17, 19, 2]

    Output: 7

    Explanation: the smallest element is 2 and its index is 7.
'''

from typing import List

def find_min_rotated(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left = 0
    right = len(arr)-1
    min_res = 0
    
    while left<=right:
        # determine the mid number
        mid = left + (right - left)//2
        # trick!!!
        # elements are divided by numbers less than or greater than the last element
        #  compare which elements are <= to the last element
        # is 50<= 20? False, go to the else condition to discard the left side
        if arr[mid] <= arr[-1]:
            min_res = mid
            right = mid -1
        else:
            left = mid + 1
    return min_res

def main():
    arr = [30, 40, 50, 10, 20]
    res = find_min_rotated(arr)
    print(res)

main()
