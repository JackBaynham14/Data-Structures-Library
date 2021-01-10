'''
This module provides the ListNode class for creating linked lists, and it contains
several methods for interacting with linked lists.
'''

class ListNode:
    '''
    Building block of a linked list that stores a data value and references the next node.
    '''
    def __init__(self, val=None):
        self.val = val
        self.next = None
    
    def __str__(self):
        return f'[{self.val}] -> {repr(self.next)}'

def fromArray(data):
    '''
    Creates a linked list from an array
    '''
    assert isinstance(data, list)

    if data == []:
        return None
    
    head = ListNode(data[0])
    head.next = fromArray(data[1:])

    return head

def toArray(head):
    '''
    Creates an array from a linked list
    '''
    assert isinstance(head, ListNode) or head is None

    if head is None:
        return []
    
    return [head.val] + toArray(head.next)

def printList(head):
    '''
    Prints out the values of a linked lis like an array
    '''
    assert isinstance(head, ListNode) or head is None

    if head is None:
        return
    
    print(head.val)
    printList(head.next)

def insert(head, val):
    '''
    Inserts a value into a sorted linked list
    '''
    assert isinstance(head, ListNode) or head is None

    if head is None:
        return ListNode(val)
    
    if val < head.val:
        newNode = ListNode(val)
        newNode.next = head.next
        head.next = newNode

        return newNode
    
    head.next = insert(head.next, val)
    
    return head

data = [1, 2, 3, 'a', 'b', 'c']
head = fromArray(data)
printList(head)
data = toArray(head)
print(data)