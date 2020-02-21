'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node, node1 = head, head

        if node == None or node.next == None:
            return node

        if node1.next:
            node1 = node1.next

        while node.val == node1.val:
            if node1.next:
                while node1.val == node1.next.val:
                    node1 = node1.next
                    if node1.next == None:
                        return
            if node == head:
                if node1.next == None:
                    return
                head = node1.next
                node = head
                if node1.next.next:
                    node1 = node1.next.next

        while node1 and node1.next:
            if node1.val == node1.next.val:
                while node1.val == node1.next.val:
                    node1 = node1.next
                    if node1.next == None:
                        node.next = None
                        break
                    node.next = node1.next
                node1 = node1.next

            else:
                node = node1
                node1 = node1.next

        return head