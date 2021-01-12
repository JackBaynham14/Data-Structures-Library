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
    assert isinstance(root, TreeNode) or root is None

    if root is None:
        return TreeNode(val)

    if val > root.val:
        return insert(root.right, val)
    else:
        return insert(root.left, val)