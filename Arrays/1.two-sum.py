# https://leetcode.com/problems/two-sum/description/
#
# Easy (46.28%)
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# You can return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,3], target = 6
# Output: [0,1]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^3
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.


def solve_hash_table(nums, target):
    
    hash_table = {}

    for index, current_val in enumerate(nums):
        
        missing_number = target - current_val
        
        if missing_number in hash_table:
            return [index, hash_table[missing_number]]
        else:
            hash_table[current_val] = index

    return -1

def solve_pointers(nums, target):
    left = 0
    right = len(nums)-1

    while left<= right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        
        if current_sum < target:
            left +=1
        
        else:
            right-=1

    return -1

def main():
    nums = [2,7,11,15] 
    target = 9
    res = solve_hash_table(nums, target)
    res2 = solve_pointers(nums, target)
    print(res2)


main()


''''
    There are 2 approaches: 
    * Array and Index has a hash key
        * Hash Table
            [2,7,11,15], target = 9
            0 1 2  3
            
            2: 0 
            7: 1

            x + y = target
            2 + 7 = 9
                2 = 9 - 7
            current_val + value in the hash table = target                 
            
            hash_table = {}

            for index, current_val in enumerate(nums):
                
                missing_number = target - current_val
                
                if missing_number in hash_table:
                    return index, hash_table[missing_number]
                else:
                    hash_table[current_val] = index
        
        * Two pointers

            left = 0
            right = len(nums)-1

            while left<= right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    return [left, right]
                
                if current_sum < target:
                    left +=1
                
                else:
                    right-=1

            return -1

'''