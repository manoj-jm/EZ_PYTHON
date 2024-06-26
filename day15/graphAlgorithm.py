# graphs algorithm 
# edges : 1 .weighted , 2.directed 
'''
spanning tree : it is a tree , which mentain a property to no of vertices should  be n-1
no of spanning trees : (n of E)+ ... + (n-1) 
eg : if vertices are 9 and edges are 13 : 
      13 + 12 + 11 + 10 + 9 + 8 = = 63

* prim's algorithm : 
      select the minimum edge vetrices
      (maintian list [f,f,f,f,f,f,f,f,f])
      slect the minimum edge at every veritces .
'''
   
#adjacency matrix 
graph = [
    [0, 7, -1, -1, -1, -1, 2, -1, -1],
    [7, 0, 4, 1, -1, 5, -1, -1, -1],
    [-1, 4, 0, -1, -1, -1, 8, -1, -1],
    [-1, 1, -1, 0, 6, 8, 3, 3, -1],
    [-1, -1, -1, 6, 0, -1, 6, 8, -1],
    [-1, 5, -1, 8, -1, 0, -1, -1, -1],
    [2, -1, 8, 3, 6, -1, 0, -1, -1],
    [-1, -1, -1, 3, 8, -1, 9, 0, -1],
    [-1, -1, -1, -1, -1, 2, -1, -1, 0]
]

visited = [False] * len(graph)
min_edge = float('inf')
x = y = -1

# Finding the initial minimum edge
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 0 or graph[i][j] == -1:
            continue
        elif min_edge > graph[i][j]:
            min_edge = graph[i][j]
            x = i
            y = j

print(x + 1, y + 1, min_edge)  # Initial minimum edge output
visited[x] = True
visited[y] = True
mst = []
mst.append((x + 1, y + 1, min_edge))

while False in visited:
    min_edge = float('inf')  # Reset the minimum edge for the next iteration
    next_x = next_y = -1  # Reset next_x and next_y for the next minimum edge

    for i in range(len(visited)):
        if visited[i]:
            for j in range(len(graph[i])):
                if graph[i][j] == 0 or graph[i][j] == -1 or visited[j]:
                    continue
                elif min_edge > graph[i][j]:
                    min_edge = graph[i][j]
                    next_x = i
                    next_y = j

    if next_y == -1:  # If no valid edge is found, break the loop
        break

    visited[next_y] = True
    mst.append((next_x + 1, next_y + 1, min_edge))

for i in mst:
    print(i,end="\n")


