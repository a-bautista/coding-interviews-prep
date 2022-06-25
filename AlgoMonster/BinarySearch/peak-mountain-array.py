from typing import List

def peak_of_mountain_array(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = left + (right - left) // 2
        # F F F T T T 
        if arr[mid] > arr[mid + 1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index

def main():
    arr = [0,10,3,2,1,0]
    res = peak_of_mountain_array(arr)
    print(res)

main()

'''
    The trick is to convert the array into the T T T F F F problem but this one is inverted, so it is F F F T T T because we want to
    know which element was the first T. 
'''