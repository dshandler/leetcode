"""
Author: Darren Shandler
Date Created: 23 January 2024
Last Edit: 28 January 2024

This python file solves a leetcode question 20. Valid Parantheses.
[Instruction]
Given a string s containing just the characters '(', ')', '{', '}', 
'[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 10**4
s consists of parentheses only '()[]{}'.
"""

class Solution:
    '''
    Class to hold the solution for the valid parantheses problem.

    Attributes:
    ------------
    None

    Methods:
    ------------
    isValid(s):
        Returns a boolean if the input string is a valid group of 
        parantheses.
    '''
        

    def isValid(self, s: str) -> bool:
        '''
        Return a boolean if the input string is a valid group of parantheses
        only containing the characters '(', ')', '{', '}', '[' and ']. A 
        valid group must have open brackets closed by the same bracket type
        and in the correct order and every closed bracket must have a 
        corresponding open bracket

        :param s str:   a string of brackets

        :return bool:   boolean if the string holds a valid group 
                        of parantheses
        '''
        openToClose = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        close = [v for _,v in openToClose.items()]
        open = []
        for b in s:
            if len(open) > 0:
                lastOpen = open[-1]
                if b in close:
                    neededToClose = openToClose[lastOpen]
                    if b == neededToClose:
                        open.pop()
                    else:
                        return False
                else:
                    open.append(b)
            else:
                if b in close:
                    return False
                else:
                    open.append(b)
            
        if len(open) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    inputs = [
        "()",
        "()[]{}",
        "(]"
    ]
    output = [
        True,
        True,
        False
    ]
    
    for i in range(len(inputs)):
        solution = Solution()
        print(f'Input list:\n{inputs[i]}')
        result = solution.isValid(inputs[i])
        print(f'Function output:\n{result}')
        print(f'Correct output:\n{output[i]}')
        print('='*50)