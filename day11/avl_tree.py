# avl tree


class node:
  def __init__(self,data) -> None:
    self.val = data
    self.left = None
    self.right = None
    self.height = 1


def insert(root,super):
  # step 1 : insert node
  # step 2 : balance factor
  # step 3 : rotation
  # step 4 : return root
  if not root:
    return node(super)
  if super < root.value:
    root.left = insert(root.left,super)
  else:
    root.right = insert(root.righ,super)


  root.height = 1 + max(getHeight(root.left),getHeight(root.right))
  # balance factor
  BF = getBF(root)


  #RR
  if  BF > 1 and super < root.left.val:
    return rightRotation(root)
  #LR
  if  BF > 1 and super > root.left.val:
    root.left = leftRotation(root.left)
    return rightRotation(root)
  
  #LL
  if BF < -1 and super > root.right.val:
    return leftRotation(root)
  #RL
  if BF <-1 and super < root.right.val:
    root.right = rightRotation(root.right)
    return leftRotation(root)
  
  return root


def inorder(root):
  if root is None:
    return
  inorder(root.left)
  print(root.val)
  inorder(root.right)

if __name__ == "__main__":
  VL = [19,98,75,7,21,34,38,27,134,100,20,0,12,17,144]
  for i in VL:
    root = insert(root,i)

  inorder(root)#if it prints in proper  order then insert function is worked well 