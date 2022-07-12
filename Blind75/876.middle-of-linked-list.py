'''
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:

head->1->2->3->4->5->NULL

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

head->1->2->3->4->5->6->NULL

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, 
we return the second one.

'''

from math import floor
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# how to get the middle?
# traverse until you find the middle?
# traverse the list twice
# one pointer to the end and set a counter to know the number of nodes
# once you have the counter then divide by two and round and go to that node to find the mid element


def my_solution(node):
    middle = 0
    res = None

    while node is not None:
        print(node.val)
        node = node.next
        middle+=1
    
    middle = floor(middle / 2)
    while node is not None:
        if node.val >= middle:
            res = node
            return res
        node = node.next


def middlenode(node):
    slow = fast = node
    while fast and fast.next:
        # the slow pointer will be at half
        slow = slow.next
        # fast is at 2.x 
        fast = fast.next.next
    return slow.val


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    res = middlenode(head)
    print(res)

main()

