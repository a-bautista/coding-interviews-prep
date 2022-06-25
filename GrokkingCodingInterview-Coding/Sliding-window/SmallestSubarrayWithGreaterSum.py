'''
    Given an array of positive integers and a number 'S', find the length of the smallest contiguous subarray whose sum is greater 
    than or equal to 'S'. Return 0 if no such subarray exists.

    Example 1:

    Input: [2, 1, 5, 2, 3, 2], S=7
    Output: 2
    Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

    Example 2:

    Input: [2, 1, 5, 2, 8], S=7
    Output: 1
    Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

    Example 3:

    Input: [3, 4, 1, 1, 6], S=8
    Output: 3
    Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

'''

def smallest_subarray_sum(target, arr):

    smallest_subarray = float('inf')
    left =0
    window_sum = 0 
    
    for right in range(len(arr)):
        window_sum += arr[right]
        while window_sum >= target:
            smallest_subarray = min(smallest_subarray, right-left+1)
            window_sum -= arr[left]
            left +=1
    
    if smallest_subarray == float('inf'):
        return 0
        
    return smallest_subarray

def main():
    arr  = [2, 1, 5, 2, 3, 2]
    arr2 = [2, 1, 5, 2, 8]
    arr3 = [3, 4, 1, 1, 6]
    S=7
    S2=8
    res = smallest_subarray_sum(S, arr2)
    print(res)

main()

