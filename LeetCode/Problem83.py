'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head:
            node = head
        else:
            return

        if node.next == None:
            return head

        node1 = node.next
        length = 1

        while node:
            if (node.val == node1.val):
                foo = node1.next
                node.next = foo
            length += 1
            if node.next:
                if node.next.val != node.val:
                    node = node.next
            if node == None:
                break
            if node.next:
                node1 = node.next
            else:
                break

        return head

