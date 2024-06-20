#traversal of graph 
# 1.DFS


def dfs(graph,src,visited_arr,stack_dfs):

  if visited_arr[src] == False:
    stack_dfs.append(src)
    visited_arr[src] = True
  else:
    return
  for i in graph[src]:
    dfs(graph,i[1],visited_arr,stack_dfs)

  print(stack_dfs.pop())

    


  


#dict to store the graph in the form of tuple (start,end,weight )
graph = {
  1:[(1,2,0),(1,3,0)],
  2:[(2,1,0),(2,7,0)],
  3:[(3,1,0),(3,6,0),(3,5,0)],
  4:[(4,7,0),(4,8,0)],
  5:[(5,3,0),(5,7,0)],
  6:[(6,3,0),(6,8,0)],
  7:[(7,4,0),(7,5,0),(7,8,0)],
  8:[(8,4,0),(8,6,0)]
}

dict_visit = {}
# keys = {1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False}
visited_arr = dict_visit.fromkeys(graph,False)
print(visited_arr)
stack_dfs = []
sr = int(input("enter the source : "))
dfs(graph,sr,visited_arr,stack_dfs)

