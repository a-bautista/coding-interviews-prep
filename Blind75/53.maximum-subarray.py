#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (47.59%)
# Likes:    11086
# Dislikes: 529
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: nums = [5,4,-1,7,8]
# Output: 23
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -10^5 <= nums[i] <= 10^5
# 
# 
# 
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
#

def solve_kadane_algo(nums):

    # edge case because the loop starts at 1
    curr_sum = max_val= nums[0]
    # max_val = float('-inf')

    for c_item in nums[1:]:
        # sum the current item 
        curr_sum+= c_item
        
        # decide if the current_item is greater than the current_sum
        curr_sum = max(c_item, curr_sum)

        # decide if the curr_sum is greater than the max val
        max_val = max(max_val, curr_sum)
    
    return max_val


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = solve_kadane_algo(nums)
    print(res)

main()


'''
    index:                      0  1   2  3   4  5  6   7  8 
    input:                    [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max(curr_sum, curr_item): [-2, 1, -2, 4,  3, 5, 6,  1, 5]
    max_val :                 [-2, 1,  1, 4,  4, 5, 6,  6, 6]


    iteration 1
    curr_item: 1
    curr_sum:  (-2+1) = 1
    
    iteration 2
    curr_item: -3
    curr_sum:  max((-3+1),-3) = -2
    
    iteration 3
    curr_item: 4
    curr_sum: max(4+(-2), 4) = 4)

    iteration 4
    curr_item: -1
    curr_sum: max(-1, 4+(-1) =3)

    iteration 5
    curr_item: 2
    curr_sum: max(2, 3+2= 5)


'''