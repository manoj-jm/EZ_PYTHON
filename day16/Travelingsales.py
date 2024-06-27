import sys



def cost(curr,visited,graph,dp):
  n = len(graph)
  if  len(visited) == n:
    return graph[curr][0]
  
  visit = tuple(visited)
  if (curr,visit) in dp:
    return dp[(curr,visit)]
  
  m=sys.maxsize

  # m=float('inf')
  for i in range(n):
    if i not in visited:
      new_visit = visited+[i]
      new_cost = graph[curr][i] + cost(i,new_visit,graph,dp)
      m = min(m,new_cost)
    dp[(curr,visit)]=m

  return m



graph = [
  [0,4,7,5,5],
  [4,0,2,3,8],
  [7,2,0,3,4],
  [5,3,3,0,6],
  [5,8,3,6,0]
]

n = len(graph)
dp = {}
print("minimum cost = ", cost(0,[0],graph,dp))