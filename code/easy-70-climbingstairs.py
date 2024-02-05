"""
Author: Darren Shandler
Date Created: 1 February 2024
Last Edit: 2 February 2024

This python file solves a leetcode question 70. Climbing Stairs.
[Instruction]
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can
you climb to the top?

Example 1:

Input: n = 1
Output 1
Explanation: There is one way to climb to the top.
1. 1 step

Example 2:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45
"""
import math

class Solution:
    '''
    Class to hold the solution for the climbing stiars problem.

    Attributes:
    ------------
    None

    Methods:
    ------------
    climbStairs(n):
        Returns the number of distinct ways one can climb to the top of
        n steps taking 1 or 2 steps at a time.
    '''
    def calcPrevious(self, n: int, previousArray: list):
        '''
        Returns the number of distinct ways one can climb at step n based
        on previous two steps 

        :param n int:               the number of steps to climb
        :param previousArray list:  array to store all previous steps
        '''
        # not possible to climb steps less than 0, return 0 distinct ways
        if n < 0:
            return 0
        # only 1 distinct way to stay in the same position
        if n == 0:
            return 1
        
        # if distinct ways of n has already been evaluated do not calcualte
        # again
        if previousArray[n] != -1:
            return previousArray[n]
        
        # distinct ways at n steps is sum of n-1 and n-2 steps
        previousArray[n] = self.calcPrevious(n - 1, previousArray) \
            + self.calcPrevious(n - 2, previousArray)
        
        return previousArray[n]



    def climbStairs(self, n: int) -> int:
        '''
        Returns the number of distinct ways one can climb to the top of
        n steps taking 1 or 2 steps at a time.

        :param n int:   the number of steps to climb

        :return int:    the number of distinct ways to climb to the top
        '''
        # create array of -1 with length n + 1 to store steps from -1 to n
        # to avoid repetition
        previousArray = [-1] * (n + 1)
        result = self.calcPrevious(n, previousArray)
        return result

if __name__ == '__main__':
    inputs = [
        2,
        3,
        4,
        5
    ]
    output = [
        2,
        3,
        5,
        8
    ]
    
    for i in range(len(inputs)):
        solution = Solution()
        print(f'Input value:\n{inputs[i]}')
        result = solution.climbStairs(inputs[i])
        print(f'Function output:\n{result}')
        print(f'Correct output:\n{output[i]}')
        print('='*50)