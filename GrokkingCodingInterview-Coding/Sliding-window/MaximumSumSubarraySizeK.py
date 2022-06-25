'''
    Given an array of positive numbers and a positive number 'k' 
    find the maximum sum of any contiguous subarray of size 'k'.

    Input: [2, 1, 5, 1, 3, 2], k=3 
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].
'''

def max_sub_array_size_k_inefficient(arr, k):
    max_sum = 0
    window_sum =0

    # len(arr) = 6 and k = 2
    # len(arr) - k + 1 you stop at 5
    # + 1 is used to count the last section of the window
    for i in range(len(arr)-k+1):
        window_sum = 0        
        # start from i and stop until the k size of the window
        for j in range(i, i+k):
            window_sum+=arr[j]
            max_sum = max(window_sum, max_sum)
    return max_sum


    for i in range(len(arr)-k+1):
        window_sum = 0
        for j in range(i, i+k):
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)
    return max_sum

def max_sub_array_size_k_optimized(arr, k):
    max_sum    = 0
    window_sum = 0 # this one contains the sum of the elements
    left = 0 # pointer for removing the starting element

    # move the window to the right
    for right in range(len(arr)):
        # add elements into this window_sum fixed to the size of k
        window_sum += arr[right]

        # when you hit the size k, start moving the window from left
        if right>=k-1:
            max_sum = max(window_sum, max_sum)

            window_sum -= arr[left]
            
            left +=1
    
    return max_sum

def main():
    arr = [2, 1, 5, 1, 3, 2]
    #      [(2+1)/6, (5+1)/6, (3+2)/6]
    k=3
    res = max_sub_array_size_k_inefficient(arr, k)
    res2= max_sub_array_size_k_optimized(arr, k)
    print(res)
    print(res2)

main()
