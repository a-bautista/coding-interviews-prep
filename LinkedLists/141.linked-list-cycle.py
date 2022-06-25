'''
    Given head, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
    Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false.


    Example 1:

    3 -> 2 -> 0 -> -4
        ^          ^
        |          |
        <-----------

    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
    Example 2:

    1 -> 2
    ^    ^
    |    |
    <----

    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
    Example 3:


    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.

'''

'''
    fast and slow pointers
    start both pointers at the head
    while the fast pointer is not None 
        move the fast pointer twice and move the slow pointer once
        if the second pointer is equal to the first one then there's a loop
'''

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


def find_cycle_length(head):
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
    if slow == fast:  # found the cycle
      return calculate_cycle_length(slow)
  return 0


def calculate_cycle_length(slow):
  current = slow
  cycle_length = 0
  while True:
    current = current.next
    cycle_length += 1
    if current == slow:
      break
  return cycle_length
        

def find_cycle(head):
    # initialize the pointers to the head
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    if slow == fast:
        return True
    return False

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  res = find_cycle(head)
  print(res)

  head2 = Node(1)
  head2.next = Node(2)
  head2.next.next = Node(3)
  head2.next.next.next = Node(4)
  head2.next.next.next.next = Node(5)
  head2.next.next.next.next.next = Node(6)
  # create the loop from node 6 to 2
  head2.next.next.next.next.next.next = head2.next.next.next
  res2 = find_cycle_length(head2)
  print(res2)


main()
