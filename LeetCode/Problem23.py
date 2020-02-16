# Merge k sorted linked lists and return it as one sorted list. Analyze and desc
# ribe its complexity.
#
#  Example:
#
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
#
#  Related Topics Linked List Divide and Conquer Heap


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return
        flag = False
        for i in lists:
            if i is not None:
                flag = True
        if flag == False:
            return
        list1 = []
        for element in lists:
            value = element
            if value is not None:
                list1.append(value.val)
                while value.next is not None:
                    list1.append(value.next.val)
                    value = value.next
        list1.sort()

        list2 = []
        for elem in list1:
            newNode = ListNode(elem)
            if len(list2) == 0:
                list2.append(newNode)
            else:
                foo = list2[0]
                while foo.next:
                    foo = foo.next
                foo.next = newNode
        return list2[0]
# leetcode submit region end(Prohibit modification and deletion)
