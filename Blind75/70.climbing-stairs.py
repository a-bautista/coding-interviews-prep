'''
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Example 1:

    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    Example 2:

    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
'''

def climbstairs(n):
    # two pointers are used to compute the next value in the sequence of the dp array bottom up
    one, two = 1, 1
    for _ in range(n-1):
        # temp will hold the previous value of one to be later used in the variable two
        temp = one 
        # one is used to calculate the next number in the sequence, you need its current value and the value of two
        one = one + two
        # assign the variable two from temp
        two = temp
    # return the value one which contains the last computed value
    return one     

def main():
    res = climbstairs(5)
    print(res)

main()
