'''
    Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

    Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

    Example 1:

    Input: s = "abccccdd"
    Output: 7
    Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
    Example 2:

    Input: s = "a"
    Output: 1
    Explanation: The longest palindrome that can be built is "a", whose length is 1.

'''

def solve(s):
    ctmap = {}
    for c in s:
        if c not in ctmap:
            ctmap[c] = 1
        else:
            ctmap[c] += 1

    ret = 0
    singleCharFound = 0

    for key in ctmap:
        # if you have an even value, then you know you can divide it to make it palindrome
        if ctmap[key] % 2 == 0:
            # get the value number for the key
            ret += ctmap[key]
        else:
            # if you find an odd value then you can convert it to an even value by subtracting one
            # the results to the ret
            ret += ctmap[key] - 1
            # keep the track of the single char value that you found because that means it can be used in 
            # the middle of the string to make it palindrome
            # ccdd_ddcc then you know either a, b or an additional d can be used in the middle to make this a palindrome
            singleCharFound = 1
    
    return ret + singleCharFound

def main():
    s = "abccccddd"
    res = solve(s)
    print(res)

main()