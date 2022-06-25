'''
    Given a string, find the length of the longest substring in it with no more than K distinct characters.

    Example 1:

    Input: String="araaci", K=2
    Output: 4
    Explanation: The longest substring with no more than '2' distinct characters is "araa".
    Example 2:

    Input: String="araaci", K=1
    Output: 2
    Explanation: The longest substring with no more than '1' distinct characters is "aa".
    Example 3:

    Input: String="cbbebi", K=3
    Output: 5
    Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
    Example 4:

    Input: String="cbbebi", K=10
    Output: 6
    Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".
'''

def longest_substring_with_k_distinct(str1, k):
    left = 0
    max_val = 0
    my_dict = {}
    window_start = 0

    for window_end in range(len(str1)):

        if str1[window_end] not in my_dict:
            my_dict[str1[window_end]]=0
        my_dict[str1[window_end]]+=1

        while len(my_dict)>k:
        # Start moving the window
            # Get the very left pointer of the window
            left = str1[window_start]

            # subtract from the dictionary because 
            my_dict[left] -=1

            if my_dict[left] == 0:
                del my_dict[left]

            window_start +=1

        max_val = max(max_val, window_end - window_start + 1)
    return max_val

def main():

    # str1 = 'araaci'
    str2 = 'aabci'
    res =  longest_substring_with_k_distinct(str2, 3)
    print(res)


main()