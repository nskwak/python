#! /usr/bin/python2.7

#'''
#####################################################################
# function: given sorted(increasing order) array, write an algorithm
# to create binary tree with minimal height
# BST : Binary Search Tree
# Cracking code page 54, 4.3
# input = [1,2,3,4,5,6,7] -> output = 4 - 2 - 1 - 3 - 6 - 5 - 7
#            4
#      2           6
#   1     3     5     7
# 4 - 2 - 1 - 3 - 6 - 5 - 7

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def sortedarraytoBST(arrayIn):
    if not arrayIn:
        return None
    mid = len(arrayIn) / 2
    root = Node(arrayIn[mid])
    print("root: ", root)
    root.left = sortedarraytoBST(arrayIn[:mid])
    root.right = sortedarraytoBST(arrayIn[mid+1:])
    return root

def preOrder(node):
    if not node:
        return
    print("%d " % node.data)
    preOrder(node.left)
    preOrder(node.right)

a = [1, 2, 3, 4, 5, 6, 7]

root = sortedarraytoBST(a)
preOrder(root)
print("\n")
#####################################################################
#'''

#'''
#####################################################################
# function: tree is balanced or not -#2
# Cracking code page 54, 4.1
#
print("===============================================================")
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def minDepth(root):
    if root is None:
        return 0
    return 1 + min(minDepth(root.left), minDepth(root.right))

def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def isBalanced(root):
    if maxDepth(root) != minDepth(root):
        print("Unbalanced")
    else:
        print("Balanced")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
#root.right.left = Node(6)
#root.right.right = Node(7)

print("max depth:", maxDepth(root))
print("min depth:", minDepth(root))
isBalanced(root)
#####################################################################
#'''


#'''
#####################################################################
# function: Find Minimum Depth of a Binary Tree -#1
# https://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/
# this problem is confusing......
print("===============================================================")
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        #print("__init__", self.data, self.left, self.right)

def minDepth(root):
    # Corner Case.Should never be hit unless the code is
    # called on root = NULL
    if root is None:
        return 0

    # Base Case : Leaf node.This acoounts for height = 1
    if root.left is None and root.right is None:
        print("11111111111111111")
        return 1

    # If left subtree is Null, recur for right subtree
    if root.left is None:
        print("22222222222222222")
        return minDepth(root.right) + 1

    # If right subtree is Null , recur for left subtree
    if root.right is None:
        print("33333333333333333")
        return minDepth(root.left) + 1

    print("44444444444444444")
    return min(minDepth(root.left), minDepth(root.right)) + 1

# Driver Program
root                = Node(1)
root.left           = Node(2)
#root.right          = Node(3)
root.left.left      = Node(4)
root.left.right     = Node(5)
#root.right.left     = Node(6)
#root.right.right    = Node(7)
print("mindepth of tree: ", minDepth(root))
#####################################################################
#'''

