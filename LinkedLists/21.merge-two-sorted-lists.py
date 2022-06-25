'''
    21. Merge Two Sorted Lists
    Easy

    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.

    L1: 1 -> 2 -> 4
    L2: 1 -> 3 -> 4
 
    1 -> 1 -> 2 -> 3 -> 4 -> 4

 
'''

# from typing import List


class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        # create a new list to store the sorted values
        dummy = ListNode(None)
        # the list that will keep track of the order from l1 and l2
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                # point to the list 1
                tail.next = l1
                # go on to the next element in list 1
                l1 = l1.next
            # l2.val > l1.val
            else:
                # point to the list 2
                tail.next = l2
                l2 = l2.next

        # in case one list doesn't contain any more values
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
              
        return dummy


def main():
    # define the nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)

    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)

    # node1.val = 1
    # node2.val = 2
    # node3.val = 4

    # node4.val = 1
    # node5.val = 3
    # node6.val = 4

    # connect the nodes
    node1.next = node2
    node2.next = node3
    node3.next = None

    node4.next = node5
    node5.next = node6
    node6.next = None

    solution = Solution()
    res = solution.mergeTwoLists(node1, node2)
    print(res)

main()
