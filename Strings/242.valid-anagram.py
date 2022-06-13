#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (57.99%)
# Likes:    2373
# Dislikes: 160
# Total Accepted:    767K
# Total Submissions: 1.3M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
# 
from collections import Counter

def solve(s, t):
    s_count = Counter(s)
    t_count = Counter(t)
    if s_count == t_count:
        return True
    return False


def main():
    s = 'car'
    t = 'rat'
    res = solve(s, t)
    print(res)

main()
        