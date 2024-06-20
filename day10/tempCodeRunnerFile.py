lst = list(map(int, input("values separated by space: ").split(' ')))
  root = Node(lst.pop(0))
  for i in lst:
      bst(i,root)
  inorder_traversal(root)