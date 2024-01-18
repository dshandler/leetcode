# Given an array of integers nums and an integer target, return indices of
# the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you 
# may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) 
# time complexity?

from operator import add

class Solution:
    # Remove comments on ValueErrors to account for constraints
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # if len(nums) < 2 | len(nums) > 105:
        #     raise ValueError('The input array must have between 2 and 104 \
        #                      (inclusive) values.')
        # elif target < -109 | target > 109:
        #     raise ValueError('The target value must be between -109 and 109 \
        #                      (inclusive)')
        nums_shift = nums.copy()
        for i in range(len(nums[:-1])):
            # if num < -109 | num > 109:
            #     raise ValueError('All numbers in the input array must be \
            #                      between -109 and 109 (inclusive)')
            
            nums_shift.append(nums_shift.pop(0))
            
            result = list(map(add, nums, nums_shift))
            if target in result:
                num_idx = result.index(target)
                num_shift_idx = num_idx + i + 1
                if num_shift_idx > len(nums):
                    num_shift_idx = num_shift_idx - len(nums)
                    return [num_shift_idx, num_idx]
                elif num_shift_idx == len(nums):
                    num_shift_idx = 0
                    return [num_shift_idx, num_idx]
                else:
                    return [num_idx, num_shift_idx]
            
        raise ValueError('No valid answer exists')

if __name__ == '__main__':
    solution = Solution()
    nums = [
        [2,7,11,15],
        [3,2,4],
        [3,3],
        [3,2,3]
    ]
    target = [
        9,
        6,
        6,
        6
    ]
    outputs = [
        [0, 1],
        [1,2],
        [0,1],
        [0,2]
    ]
    problem = 3
    result = solution.twoSum(nums[problem], target[problem])
    print(nums[problem])
    print(target[problem])
    print('Solution:')
    print(result)