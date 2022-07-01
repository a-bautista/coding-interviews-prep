#
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (61.28%)
#
# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
# 
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# 
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# 
# 
# Follow up:
# 
# 
# Could you solve it in O(n) time complexity and without using division?
# Could you solve it with O(1) constant space complexity? (The output array
# does not count as extra space for space complexity analysis.)
# 
# 

def solve_brute_force(nums):
    res = []
    for i, _ in enumerate(nums):
        temp_mult = 1
        for j, j_val in enumerate(nums):
            if i != j:
                temp_mult *= j_val
        res.append(temp_mult)
    return res

def optimal_solution(nums):
    res = [1 for _ in range(len(nums))]

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix*=nums[i]

    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    
    return res


    '''
        [1, 1, 1, 1]



    
    '''


def main():
    nums = [1,2,3,4]
    res = solve_brute_force(nums)
    res2 = optimal_solution(nums)
    print(res2)

main()

'''
    # Input: nums = [1,2,3,4]
    # Output: [24,12,8,6]
'''
