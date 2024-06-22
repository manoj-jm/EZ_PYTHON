def levelorder(root):
  q =[root]
  q.append(None)
  while len(q)>0:
    curr = q.pop(0)
    if curr == None:
      if len(q)==0:
        break
      else:
        print()
        q.append(None)
    else:
      print(curr.value,end='')
      if curr.left != None:
        q.append(curr.left)
      if curr.right !=None:
        q.append(curr.right)