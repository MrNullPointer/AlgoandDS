'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        length = 0
        node = head
        newList = []

        while node:
            length += 1
            newList.append(node.val)
            node = node.next

        if length <= 1:
            return head

        quotient = len(newList) // 2
        rem = len(newList) % 2

        if rem == 1:
            length1 = len(newList) - 1
        else:
            length1 = len(newList)

        for i in range(0, length1, 2):
            foo = newList[i]
            newList[i] = newList[i + 1]
            newList[i + 1] = foo

        newL = ListNode(newList[0])

        for j in range(1, len(newList)):
            newNode = ListNode(newList[j])
            xoo = newL
            while xoo.next:
                xoo = xoo.next
            xoo.next = newNode

        return newL

