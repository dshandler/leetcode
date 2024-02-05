"""
Author: Darren Shandler
Date Created: 4 February 2024
Last Edit: 5 February 2024

This python file solves a leetcode question 94. Binary tree inorder traversal.
[Instruction]
Given the root of a binary tree, return the inorder traversal of its 
nodes' values.

Example 1:
        (1)
           \
            \
            (2)
            /
           /
        (3) 

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    '''
    Class to hold the Tree Node.

    Attributes:
    ------------
    val:    int
    left:   int
    right:  int

    Methods:
    ------------
    __init__(val=0, left=None, right=Nonw):
        initialise the TreeNode class
    '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Class to hold the solution for the binary tree inorder traversal problem.

    Attributes:
    ------------
    result: list
    stack:  list

    Methods:
    ------------
    inorderTraversal(root, solution_type):
        Returns the inorder traversal of the node values of the binary tree.
    iterative(root):
        Generates the inorder traversal by iteratively progressing through
        the binary tree.
    recursive(root):
        Generates the inorder traversal by recursivly progressing through
        the binary tree
    '''
    def __init__(self):
        self.result = []
        self.stack = []

    def inorderTraversal(
            self,
            root: Optional[TreeNode],
            solution_type = "iterative"
        ) -> list[int]:
        '''
        Return a list of integers of the indices of the two numbers 
        that add up to the target.

        :param root TreeNode:       the root of TreeNode class
        :param solution_type str:   specifying the method of inorder traversal
                                    either iterative (default) or recursive

        :return list:       a list of the inorder traversal
        '''
        if solution_type == "iterative":
            self.iterative(root)
        else:
            self.recursive(root)
        return self.result
    
    def iterative(self, root: Optional[TreeNode]):
        '''
        Iterates through the Binary Tree to produce the inorder traversal,
        stored in the class attribute result.

        :param root TreeNode:   the root of TreeNode class
        '''
        if root is not None:
            node = root
            while True:
                # while the node is not None
                while node is not None:
                    # add the root of the tree to the stack
                    self.stack.append(node)
                    # continue down furthest left node till None
                    node = node.left
                # If the stack is empty the tree has been traversed
                if len(self.stack) == 0:
                    return
                # retrieve next node from the stack
                node = self.stack.pop()
                # append the value of the current node to the result
                self.result.append(node.val)
                # traverse to the next right node up one level from the stack
                node = node.right
                

    def recursive(self, root: Optional[TreeNode]):
        '''
        Recursively perform inorder traversal on a binary Tree.

        :param root TreeNode:   the root of TreeNode class
        '''
        if root:
            self.recursive(root.left)
            self.result.append(root.val)
            self.recursive(root.right)


if __name__ == '__main__':
    inputs = [
        [1,None,2,3],
        [],
        [1]
    ]
    output = [
        [1,3,2],
        [],
        [1]
    ]
    print(f'Input list:\n{inputs[0]}')
    solution = Solution()
    root = TreeNode(inputs[0][0])
    root.right = TreeNode(inputs[0][2])
    root.right.left = TreeNode(inputs[0][3])
            
    result = solution.inorderTraversal(root)
        
    print(f'Function output:\n{result}')
    print(f'Correct output:\n{output[0]}')
    print('='*50)
    
    print(f'Input list:\n{inputs[1]}')
    solution = Solution()
    root = None
    result = solution.inorderTraversal(root)
    print(f'Function output:\n{result}')
    print(f'Correct output:\n{output[1]}')
    print('='*50)

    print(f'Input list:\n{inputs[2]}')
    solution = Solution()
    root = TreeNode(inputs[2][0])
    result = solution.inorderTraversal(root)
    print(f'Function output:\n{result}')
    print(f'Correct output:\n{output[2]}')
    print('='*50)