'''
    Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters 
    from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.

    Example 1:

    Input: ransomNote = "a", magazine = "b"
    Output: false
    Example 2:

    Input: ransomNote = "aa", magazine = "ab"
    Output: false
    Example 3:

    Input: ransomNote = "aa", magazine = "aab"
    Output: true
'''

def my_solution(ransomNote, magazine):
    hash_magazine = {}
    hash_r = {}

    for r in ransomNote:
        if r in hash_r:
            hash_r[r]+=1
        else:
            hash_r[r]=1

    for l in magazine:
        if l in hash_magazine:
            hash_magazine[l]+=1
        else:
            hash_magazine[l]=1
            
    # subtract the letters from the magazine that are used in the ransom note
    for letter in ransomNote:
        if letter not in hash_magazine:
            hash_magazine[letter] =0
        if hash_magazine[letter]>0:
            hash_magazine[letter]-=1
            hash_r[letter]-=1

    for letter in ransomNote:
        # the magazine dict should always contain more letters available than in the ransom note, if this is not the case
        # then return False
        if hash_magazine[letter]<hash_r[letter]:
            return False
    return True

def solve_better(ransomNote, magazine):
    for i in set(ransomNote):
        # if there are less letters in the magazine than in the ransom note then there's a problem
        if magazine.count(i) < ransomNote.count(i):
            return False
    return True


def main():

    ransomNote = "aa"
    magazine = "aab"
    res = my_solution(ransomNote, magazine)
    print(res)
    # ransomNote = "bg"
    # magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
    # "fihjjjjei"
    # "hjibagacbhadfaefdjaeaebgi"
    # "bg"

main()