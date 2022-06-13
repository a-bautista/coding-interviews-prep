def binary_search(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] < target:
            left += 1
        else:
            right-=1
    return -1
        