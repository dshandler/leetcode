"""
Author: Darren Shandler
Date Created: 28 January 2024
Last Edit: 28 January 2024

This python file solves a leetcode question 21. Merge two sorted lists
[Instruction]
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    '''
    Class to hold the List Node.

    Attributes:
    ------------
    val
    next

    Methods:
    ------------
    __init__(val=0, next=None):
        initialise the ListNode class
    '''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class createListNode:
    '''
    class to create a list node from integers
    
    Attributes:
    ------------
    listOfNodes : List
        The list containing the list nodes.
    

    Methods:
    ------------
    __init__():
        Initialise the createListNode class
    addToListNode(val):
        Adds a new value to the end of the ListNode
    getList():
        Returns the ListNode
    '''
    def __init__(self):
        self.listNode = None
        
        
    def addToListNode(self, new_val):
        '''
        Adds a new integer to a listNode
        
        :param new_val int: an integer to be added to a ListNode
        '''
        newNode = ListNode(new_val)
        if self.listNode is None:
            self.listNode = newNode
        else:
            lastNode = self.listNode
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next = newNode

    def getList(self):
        '''
        Returns the listNode

        :return ListNode:   returns the listNode
        '''
        return self.listNode
        

class Solution:
    '''
    Class to hold the solution for the merge two sorted lists problem where
    both input lists are already sorted.

    Attributes:
    ------------
    None

    Methods:
    ------------
    mergeTwoLists(list1, list2):
        Returns a sorted ListNode of list1 and list2.
    '''
    def mergeTwoLists(
            self, 
            list1: Optional[ListNode], 
            list2: Optional[ListNode]
        ) -> Optional[ListNode]:
        '''
        Merges two lists of type ListNode into a sorted ListNode

        :param list1 ListNode:  a sorted ListNode to be merged with list2
        :param list2 ListNode:  a sorted ListNode to be merged with lsit1

        :return ListNode:       a sorted ListNode of list1 and list2 merged
                                together
        '''
        
        mergedList = ListNode()
        lastNode = mergedList
        while True:
            if list1 is None:
                lastNode.next = list2
                break
            if list2 is None:
                lastNode.next = list1
                break

            if list1.val >= list2.val:
                lastNode.next = list2
                list2 = list2.next
            else:
                lastNode.next = list1
                list1 = list1.next

            lastNode = lastNode.next
            
        return mergedList.next
    


if __name__ == '__main__':
    list1 = [
        [1,2,4],
        [],
        [],
        [8]
    ]
    list2 = [
        [1,3,4],
        [],
        [0],
        [1,3,3,5]
    ]
    output = [
        [1,1,2,3,4,4],
        [],
        [0],
        [1,3,3,5,8]
    ]
    
    for i in range(len(output)):
        solution = Solution()
        print(f'Input 1 list:\n{list1[i]}')
        print(f'Input 2 list:\n{list2[i]}')
        list1Node = createListNode()
        for node in list1[i]:
            list1Node.addToListNode(node)
        list2Node = createListNode()
        for node in list2[i]:
            list2Node.addToListNode(node)
        result = solution.mergeTwoLists(
            list1Node.getList(),
            list2Node.getList()
        )
        result_list = []
        while result is not None:
            result_list.append(result.val)
            result = result.next
            
        print(f'Function output:\n{result_list}')
        print(f'Correct output:\n{output[i]}')
        print('='*50)