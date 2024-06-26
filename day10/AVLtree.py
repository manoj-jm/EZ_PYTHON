# binary search tree using list
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#best first search
def bst(val,root):
    if root is None:
        return Node(val)
    else:
        if val < root.val:
            root.left = bst(val,root.left)
        elif val > root.val:
            root.right = bst(val,root.right)
        return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

if __name__ == '__main__':
    lst = list(map(int, input("values separated by space: ").split(' ')))
    root = Node(lst.pop(0))
    for i in lst:
        bst(i,root)
    inorder_traversal(root)