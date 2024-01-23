"""
Author: Darren Shandler
Date Created: 18 January 2024
Last Edit: 23 January 2024

This python file solves a leetcode question 13. Roman to Integer.
[Instruction]
Roman numerals are represented by seven different symbols: I, V, X, L, C, D 
and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added 
together. 12 is written as XII, which is simply X + II. The number 27 
is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is 
written as IV. Because the one is before the five we subtract it making 
four. The same principle applies to the number nine, which is written as 
IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

"""

class Solution:
    '''
    Class to hold the solution for the roman to integer problem.

    Attributes:
    ------------
    chatToIntDict : dict
        Dictionary holding the value conversion from the base roman numerals
        values to integer value

    Methods:
    ------------
    romanToInt(s):
        Returns the integer value of the roman numerals input string.
    '''
    def __init__(self):
        self.charToIntDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            '0': 0
        }
    def romanToInt(self, s: str) -> int:
        '''
        Returns the integer value of the roman numerals input string

        :param s str:   string of roman numerals

        :return int: integer value of roman numerals string input
        '''
        if len(s) < 1 | len(s) > 15:
            raise ValueError('The length of the input string must be between \
                             1 and 15 characters (inclusive)')
        result = 0
        for i in range(len(s)-1):
            intN = self.charToIntDict[s[i]]
            intN1 = self.charToIntDict[s[i+1]]
            if intN < intN1:
                result -= intN
            else:
                result += intN
        return result + self.charToIntDict[s[-1]]


if __name__ == '__main__':

    s = [
        "III",
        "LVIII",
        "MCMXCIV",
        "CMXCIX",
        "MCMLXXXVIII"
    ]
    output = [
        3,
        58,
        1994,
        999,
        1988
    ]
    for i in range(len(s)):
        solution = Solution()
        print(f'Input list:\n{s[i]}')
        result = solution.romanToInt(s[i])
        print(f'Function output:\n{result}')
        print(f'Correct output:\n{output[i]}')
        print('='*50)

