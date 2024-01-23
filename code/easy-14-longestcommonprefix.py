"""
Author: Darren Shandler
Date Created: 23 January 2024
Last Edit: 23 January 2024

This python file solves the leetcode problem 14. Longest common prefix.
[Instruction]
Write a function to find the longest common prefix string amongst an 
array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

class Solution:
    '''
    Class to hold the solution for the longest common prefix problem.

    Attributes:
    ------------
    None

    Methods:
    ------------
    longestCommonPrefix(strs):
        Returns a string of the longest common prefix to all strings inside
        the input list.
    '''
    def longestCommonPrefix(self, strs: list[str]) -> str:
        '''
        Returns a string of the longest common prefix to all strings inside
        the input list. If there is no common prefix, an empty list is
        returned.

        :param strs list:   list of strings to compare

        :return str:        the longest common prefix of all strings
        '''
        if len(strs) < 1 | len(strs) > 200:
            raise ValueError('The length of the input list must be between \
                             1 and 200 (inclusive).')
        elif len(strs) == 1:
            return strs[0]
        else:
            common_list = list(strs[0])
            smallest = common_list
            for str in strs[1:]:
                str_list = list(str)
                if len(str_list) < len(smallest):
                    smallest = str_list
                common_length = len(smallest)

                same_chars = 0
                for i in range(common_length):
                    if common_list[i] == str_list[i]:
                        same_chars += 1 
                    else:
                        smallest = smallest[:same_chars]
                        break 
                    
                if len(smallest) == 0:
                    return ''
            return ''.join(smallest)


if __name__ == '__main__':

    strs = [
        ["flower","flow","flight"],
        ["dog","racecar","car"],
        ["ab", "a"],
        ["aaa","aa","aaa"]
    ]
    output = [
        "fl",
        "",
        "a",
        "aa"
    ]
    for i in range(len(strs)):
        solution = Solution()
        print(f'Input list:\n{strs[i]}')
        result = solution.longestCommonPrefix(strs[i])
        print(f'Function output:\n{result}')
        print(f'Correct output:\n{output[i]}')
        print('='*50)