'''
    67. Add Binary
    Given two binary strings a and b, return their sum as a binary string.

    

    Example 1:

    Input: a = "11", b = "1"
    Output: "100"
    Example 2:

    Input: a = "1010", b = "1011"
    Output: "10101"
'''

class Solution:
    def addBinary(self, a, b):    
        # string value
        res = ""
        carry = 0
        
        # you need to invert the values of the strings, to add them in order
        a, b = a[::-1], b[::-1]
        # you will iterate through the longest string
        for i in range(max(len(a), len(b))):
            # convert the string values to integers
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            # add the binary values            
            total = digitA + digitB + carry
            
            # convert the total to binary
            char = str(total % 2)
            # add the strings
            res = char + res
            # add the carry
            carry = total // 2
            # print(f"Digit A:{digitA} \n Digit B:{digitB}")

        if carry:
            # add 1 to the res because that's the value of the carry
            res = "1" + res

        return res

def main():

    a = "100"
    b ="11"
    sol = Solution()
    res = sol.addBinary(a, b)
    print(res)

main()

