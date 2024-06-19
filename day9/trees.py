class node:
  def __init__(self,data) -> None:
    self.value = data
    self.right = None
    self.left = None


def preorder(root):
  if root == None:
    return
  print(root.value)
  preorder(root.left)
  preorder(root.right)

def postorder(root):
  if root == None:
    return
  postorder(root.left)
  postorder(root.right)
  print(root.value)

def inorder(root):
  if root == None:
    return
  inorder(root.left)
  print(root.value)
  inorder(root.right)

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
      
#depth or height of the tree
def depth(root):
  if root == None:
    return 0
  leftheight = depth(root.left)
  rightheight = depth(root.right)

  return max(leftheight,rightheight)+1

def leafnodes(root):
  if root is None:
    return 
  
  # q = [root]
  
  # while q:
  #   curr = q.pop(0)
  if root.left == None and root.right == None:
    print(root.value , end=' ')
  if root.left!=None:
    leafnodes(root.left)
  if root.right!=None:
    leafnodes(root.right)


if __name__ == "__main__":
  root = node(1)

  root.left = node(2)
  root.right = node(3)

  root.left.left = node(4)
  root.left.right = node(5)

  root.right.left = node(6)
  root.right.right = node(7)

  root.right.right.left = node(10) # 4th level
  root.right.right.left.right = node(19) # 5th level


  print("pre order : \n")  
  preorder(root)
  print("post order : \n")
  postorder(root)
  print("In order : \n")
  inorder(root)
  print("level order")
  levelorder(root)
  print("\nheight of the tree :", depth(root))
  print("leaf nodes of tree : ")
  leafnodes(root)