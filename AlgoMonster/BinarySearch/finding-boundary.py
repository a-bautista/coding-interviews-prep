'''
    An array of boolean values is divided into two sections; the left section consists of all false and the right section consists of all true. Find the boundary of the right section, i.e. the index of the first true element. If there is no true element, return -1.

    Input: arr = [false, false, true, true, true]

    Output: 2

    Explanation: first true's index is 2.
'''

def find_boundary(arr):
    left, right = 0, len(arr) - 1
    # set to -1 in case you don't find any value
    boundary_index = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid]:
            boundary_index = mid
            # I found a True value in the middle  but I don't know if this is the first True value, so I need to discard the right side
            right = mid -1
        else:
            # I didn't find any True value in the middle, then discard the left side 
            left = mid + 1
    return boundary_index

def main():
    test_1 = [False, False, True, True, True]
    test_2 = [True, True, True, True, True]
    test_3 = [True]
    test_4 = [False, False, False]
    res = find_boundary(test_1)
    print(res)

main()