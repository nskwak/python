#! /usr/bin/python2.7
#####################################################################
# https://medium.com/@sarahelson81/top-15-interview-questions-for-test-automation-engineers-e6c20842910
# Question 3
# Write a program to find the depth of binary search tree, without using recursion.
print("====================== Question 3 ===========================")
#'''
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def minDepth(root):
    if(root is None):
        return 0
    return (1 + min(minDepth(root.left), minDepth(root.right)))

def maxDepth(root):
    if(root is None):
        return 0
    return (1 + max(maxDepth(root.left), maxDepth(root.right)))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(40)
root.left.left.right = Node(41)
rst = minDepth(root)
print("minDepth:", rst)
rst = maxDepth(root)
print("maxDepth:", rst)
#'''


'''
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
'''