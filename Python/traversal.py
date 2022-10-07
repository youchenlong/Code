from binarytree import *

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.left.left.left = Node('F')
root.left.left.right = Node('G')
root.left.left.right.left = Node('H')
root.left.left.right.right = Node('I')


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.value, end=' ')
    inorder(root.right)

def preorder(root):
    if root is None:
        return
    print(root.value, end=' ')
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value, end=' ')

inorder(root)
preorder(root)
postorder(root)