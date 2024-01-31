"""
Author: Darren Shandler
Date Created: 31 January 2024
Last Edit: 31 January 2024

This python file solves a leetcode question 35. Search Insert Position.
[Instruction]
Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were 
inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

class Solution:
    '''
    Class to hold the solution for the search insert position problem.

    Attributes:
    ------------
    None

    Methods:
    ------------
    searchInsert(nums, target):
        Returns the index that matches the target or insertion index.
    '''

    def searchInsert(self, nums: list[int], target: int) -> int:
        '''
        Return the index of a sorted array that matches the target
        or the index where the target would be inserted.

        :param nums list:   a list of integers
        :param target int:  a target integer value 

        :return int:       the index location or insertion index
        '''
        # Calculate lower and upper bounds
        left = 0
        right = len(nums)
        # Continue iterating until search space has length 1
        while left < right:
            half_len = (right + left) // 2
            # If target at centre - found location
            if target == nums[half_len]:
                return half_len
            # If target in lower half or upper half, 
            # reduce search space by half
            if target < nums[half_len]:
                right = half_len
            else:
                left = half_len + 1
        # If reduced search space to length 1, location to right
        return right

if __name__ == '__main__':
    inputs = [
        [1,3,5,6],
        [1,3,5,6],
        [1,3,5,6],
        [1,3,5]
    ]
    target = [
        5,
        2,
        7,
        4
    ]
    output = [
        2,
        1,
        4,
        2
    ]
    
    for i in range(len(inputs)):
        solution = Solution()
        print(f'Input list:\n{inputs[i]}')
        print(f'Targett:\n{target[i]}')
        result = solution.searchInsert(inputs[i], target[i])
        print(f'Function output:\n{result}')
        print(f'Correct output:\n{output[i]}')
        print('='*50)