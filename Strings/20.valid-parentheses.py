'''
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

    Example 1:

    Input: s = "()"
    Output: true
    Example 2:

    Input: s = "()[]{}"
    Output: true
    Example 3:

    Input: s = "(]"
    Output: false
'''

'''

edge cases:

    "" what do we return ?

Examples

    True
    ( ) [ ] { }
    0 1 2 3 4 5 

    balanced

    False
    ( ) [ ] { 
    0 1 2 3 4 5 

    pop {

    not balanced

    strs = '()'

    opening = set('{','[','(')
    # closing = set('}', ']', ')')
    stack = []
    
    for i in range(len(strs)):
        if strs[i] in opening:
            stack.append(strs[i])
        else:
            if not stack: 
                return False

            # last_element = stack[-1]
            if (stack[-1]!='(' and strs[i]!=')') or (stack[-1]!='{' and strs[i]!='}') or (stack[-1]!='[' and strs[i]!=']'):
                return False
            stack.pop()
    return True


'''

def solve(strs):
    
    if len(strs) == 0:
        return False

    stack = []
    for i in range(len(strs)):
        if strs[i] == '(' or strs[i] == '[' or strs[i] == '{':
            stack.append(strs[i])
        else:
            if not stack:
                return False
            if (stack[-1] != '(' and strs[i] == ')') or (stack[-1] != '{' and strs[i] == '}') or (
                    stack[-1] != '[' and strs[i] == ']'):
                return False
            stack.pop()

    return True if len(stack)==0 else False

def main():

    s = "()[]{"
    res = solve(s)
    print(res)

main()