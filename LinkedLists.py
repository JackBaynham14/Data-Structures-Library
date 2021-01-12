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
    assert head is None or isinstance(head, ListNode)

    if head is None:
        return []
    
    return [head.val] + toArray(head.next)

def printList(head):
    '''
    Prints out the values of a linked list
    '''
    assert head is None or isinstance(head, ListNode)

    if head is None:
        return
    
    print(head.val)
    printList(head.next)

def insert(head, val):
    '''
    Inserts a value into a sorted linked list
    '''
    assert head is None or isinstance(head, ListNode)
    assert head is None or type(val) == type(head.val)

    if head is None:
        return ListNode(val)
    
    if val < head.val:
        newNode = ListNode(val)
        newNode.next = head.next
        head.next = newNode

        return newNode
    
    head.next = insert(head.next, val)

    return head