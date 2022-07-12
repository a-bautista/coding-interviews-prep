'''
    206. Reverse Linked List
    Easy

    Add to List

    Share
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    head->1->2->3->4->5->NULL

    NULL->5->4->3->2->1->HEAD

    You can solve this iteratively or recursively.
 
'''
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next

def reverseList(head):
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev # reverse the linked list
        prev = curr # move the lower cursor to the value of current
        curr = temp # move to the next node by using the temp value
    return prev

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverseList(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

main()



