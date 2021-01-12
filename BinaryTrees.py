'''
This module provides the TreeNode class for creating a binary search tree, and it
contains several methods for interacting with trees.
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    '''
    Inserts a value into a binary search tree
    '''
    assert root is None or isinstance(root, TreeNode)
    assert root is None or type(val) == type(root.val)

    if root is None:
        return TreeNode(val)

    if val > root.val:
        root.right = insert(root.right, val)
    else:
        root.left = insert(root.left, val)
    
    return root

def fromArray(data, root=None):
    '''
    Creates a binary search tree from an array
    '''
    assert isinstance(data, list)

    if data == []:
        return
    
    root = fromArray(data[:-1], root)
    return insert(root, data[-1])