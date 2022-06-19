'''
    Given an integer, find its square root without using the built-in square root function. 
    Only return the integer part (truncate the decimals).

    Input: 16

    Output: 4

    Input: 8

    Output: 2

    Explanation: square root of 8 is 2.83..., return integer part 2
'''
def square_root(n):
    if n == 0:
        return 0

    left, right = 1, n
    res = -1
    while left <= right:
        mid = left + (right - left) //2
        # this is like finding the target
        # if mid**2 is equal to or less than n then you have a possible sqrt number
        # but you need to discard the left side from middle
        if mid * mid <= n:
            res = mid
            left = mid + 1
        # discard the right side
        else: 
            right = mid - 1
    return res

def main():
    res = square_root(16)
    print(res)

main()