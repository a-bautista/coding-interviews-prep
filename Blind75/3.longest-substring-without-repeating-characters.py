# 3. Longest Substring Without Repeating Characters
# Medium

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Input: s = "abcabcbb"
# Output: 0
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

from collections import Counter
def solve(s):
    if not s or "":
        return 0
    
    # if len(s) == 1:
    #     return 1
    
    # window = ""
    # max_window = float('-inf')
    # for c_letter in s:
    #     window+=c_letter
    #     count = Counter(window)
    #     if int(max(count.values()))>1:
    #         # subtract the previous code
    #         window= window[:-1]
    #         max_window = max(len(window), max_window)
    #         #
    #         window = c_letter
    #     else:
    #         max_window = max(len(window), max_window)
    # return max_window

    j = 0
    # build a hash table from a set
    unique_letters = set()
    res = 0
    for i in range(len(s)):
        # get all the unique letters in a substring 
        while j<len(s) and s[j] not in unique_letters:
            unique_letters.add(s[j])
            # move the front part of the window j forward
            j+=1

        # j-i is used to subtract the window different of the unique letters
        res = max(res, j-i)
        # remove the initial letter because you need to move the back of the window (i) forward 
        unique_letters.remove(s[i])

    return res

def main():
    res = solve('dvdf')
    print(res)

main()