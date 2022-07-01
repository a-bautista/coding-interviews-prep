from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hash table to count the number of occurrences
        my_dict = {}
        max_val = float('-inf')
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]] = 0
            my_dict[nums[i]] += 1

        # do the comparison  index with index, values with values    
        for index, value in (my_dict.items()):
            if value > max_val:
                # the variable changes
                max_val = value
                index_val = index
        return index_val

def main():
    nums = [2,2,1,1,1,2,2]
    sol = Solution()
    res = sol.majorityElement(nums)
    print(res)

main()
