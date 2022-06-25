# 438. Find All Anagrams in a String
# Medium

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
 
# Constraints:

# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.

from collections import Counter
def my_solution(s, p):
    counter = Counter(p) 
    # counter =
    #     {
    #         a: 1
    #         b: 1
    #         c: 1
    #     }

    indexes = []
    j=0
    for i in range(len(s)):
        if s[i] in p:
            counter[s[i]]-=1

        else:
            # reset the counter
            counter = Counter(p)
            indexes.append(j)
            j=i

    return indexes


def neetcode_solution(s, p):

    # in case the window p is greater than the string s, return []
    if len(p)> len(s): 
        return []
    
    pCount, sCount = {}, {}
    
    # populate the counters
    for i in range(len(p)):
        # in case the key doesn't exist in the dictionary then use .get
        # if the key exists to get the value that is pointing
        # if there's no key then use the value 0
        # pCount[p[i]] = 1 + pCount.get(p[i], 0)
        # sCount[s[i]] = 1 + sCount.get(s[i], 0)
        if p[i] not in pCount:
            pCount[p[i]] = 0
        if s[i] not in sCount:
            sCount[s[i]] = 0
        pCount[p[i]]+=1
        sCount[s[i]]+=1
        
    # check if the counters already contain any anagram
    # if so, then add 0 because that's the index
    # else return an empty []
    res = [0] if pCount == sCount else []
    left = 0
    for right in range(len(p), len(s)):
        
        # move the window

        # add a value to the right and make sure that if the key doesn't exist 
        # then add the key with a 0 
        
        sCount[s[right]] = 1 + sCount.get(s[right], 0)
        
        # remove the left pointer from the sCount 
        sCount[s[left]] -=1 
        
        # remove the left pointer if it is zero
        if sCount[s[left]] == 0:
            sCount.pop(s[left])
        
        # move to the next value in the sCount
        left +=1
        
        # end of the window
        # check if counters are the same, so you can add the indexes
        # left indexes because that's where you start
        if sCount == pCount:
            res.append(left)
            
    return res
            
def my_solution(p, q):
    pDict = {}
    qDict = {}
    window_start = 0
	
    for i in range(len(q)):
        if p[i] not in pDict:
            pDict[p[i]] = 0
        if q[i] not in qDict:
            qDict[q[i]] = 0

    pDict[p[i]] += 1
    qDict[q[i]] += 1

    res = 0 if pDict == qDict else []

    for window_end in range(len(q), len(p)):

        if pDict[window_end] == 0:
            pDict[window_end] = 0
        pDict[window_end] += 1

        left = p[window_start]

        pDict[left] -= 1

        if pDict[left] == 0:
            del pDict[left]

        if pDict == qDict:
            res.append(window_start)

        window_start += 1

    return res
		

def main():
    s = 'cbaebabacd'
    p = 'abc'
    res = neetcode_solution(s, p)
    res2 = my_solution(s, p)
    print(res)
    print(res2)

main()

'''

s = c b a e b a b a c 
i = 0 1 2 3 4 5 6 7 8

substr = 'abc'

trick!!!

counter = Count(s)
counter =
    {
        a: 1
        b: 1
        c: 1
    }

initial_index = 0
indexes = []
j=0
for i in range(len(s)):
    if s[i] in substr:

    # if initial_index == 0:
    #     indexes.append(i)
    #     initial_index +=1

        # decrease the count in the counter
        counter[s[i]]-=1

    else:

        # reset the counter
        counter = Count(s)
        indexes.append(j)
        j=i

return indexes





start decreasing each count of letter whenever it appears in the string

for i in range(len(s)):
    if s[i] in substr:







s = "cbaebabacd", p = "abc"

'''