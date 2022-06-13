# 125. Valid Palindrome
# Easy

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

def solve_not_optimal(word):
    return word==word[::-1]

def solve(s):

    cleaned_word = s.lower()     
    left = 0
    right = len(cleaned_word)-1
    
    while left<=right:

        while left < right and not cleaned_word[left].isalnum():
            left+=1
        
        while left < right and not cleaned_word[right].isalnum():
            right-=1

        if cleaned_word[left]!=cleaned_word[right]:
            return False

        left+=1
        right-=1
    return True
    
def main():
    word = "A man, a plan, a canal: Panama"
    res = solve(word)
    print(res)

main()