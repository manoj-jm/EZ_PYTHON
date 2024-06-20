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


#level order / BSF
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

def top_view(root):
  if root is None:
        return
  # Dictionary to store the top view of the binary tree
  top_view_dict = {}

  # Queue to perform level order traversal
  # It stores tuples of (node, horizontal_distance)
  queue = [(root, 0)]

  while queue:
      node, hd = queue.pop(0)
      if node == None:
        if len(queue)==0:
          break
        else:
          print()
          queue.append(None)
      else:
      # If the horizontal distance is encountered for the first time
        if hd not in top_view_dict:
            top_view_dict[hd] = node.value

        # Move to the left child
        if node.left:
            queue.append((node.left, hd - 1))
        # Move to the right child
        if node.right:
            queue.append((node.right, hd + 1))

  # Extracting the top view nodes from the dictionary
  for hd in sorted(top_view_dict):
      print(top_view_dict[hd], end=" ")



def bottomview(root):
  if root is None:
    return
  top_view_dict = {}

  # Queue to perform level order traversal
  # It stores tuples of (node, horizontal_distance)
  queue = [(root, 0)]

  while queue:
      node, hd = queue.pop(0)
      if node == None:
        if len(queue)==0:
          break
        else:
          print()
          queue.append(None)
      else:
      # If the horizontal distance is encountered for the first time
        top_view_dict[hd] = node.value

        # Move to the left child
        if node.left:
            queue.append((node.left, hd - 1))
        # Move to the right child
        if node.right:
            queue.append((node.right, hd + 1))

  # Extracting the bottom view nodes from the dictionary
  for hd in sorted(top_view_dict):
      print(top_view_dict[hd], end=" ")
  
def leftview(root): # sir's method 
  if root is None:
    return
  q =[root]
  q.append(None)
  while len(q)>0:
    curr = q.pop(0)
    if curr == None:
      if len(q)==0:
        break
      else:
        print(q[0].value)
        q.append(None)
    else:
      if curr.left != None:
        q.append(curr.left)
      if curr.right !=None:
        q.append(curr.right)

def rightview(root): # sir's method 
  if root is None:
    return
  q =[root]
  q.append(None)
  while len(q)>0:
    curr = q.pop(0)
    if curr == None:
      if len(q)==0:
        break
      else:
        print(q[-1].value)
        q.append(None)
    else: 
      if curr.left != None:
        q.append(curr.left)
      if curr.right !=None:
        q.append(curr.right)
  
  

if __name__ == "__main__":
  root = node(1)

  root.left = node(2)
  root.right = node(3)

  root.left.left = node(4)
  root.left.right = node(5)


  root.left.left.left = node(55)
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
  print("\ntop view")
  top_view(root)
  print("\nbottom view")
  bottomview(root)
  print("\nleft view")
  leftview(root)
  print('\nright veiw')
  rightview(root)