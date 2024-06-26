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
adja_Matrix=[[0,11,7,1,-1,-1],
             [11,0,3,-1,4,-1],
             [7,3,0,-1,4,-1],
             [1,-1,5,0,-1,2],
             [-1,4,-1,-1,0,-1],
             [-1,-1,-1,2,-1,0]]
visited=[False]*len(adja_Matrix)
min=float("inf")
for i in range(len(adja_Matrix)):
    for j in range(len(adja_Matrix[i])):
        if adja_Matrix[i][j]<min and adja_Matrix[i][j]>0 :
            min=adja_Matrix[i][j]
            pos=i
            pos1=j
    visited[pos]=visited[pos1]=True
spanning_tree=[(pos+1,pos1+1,min)]
while False in visited:
    min=float('inf')
    for i in range(len(visited)):
        if visited[i]==True:
            for j in range(len(adja_Matrix[i])):
                if adja_Matrix[i][j]>0 and adja_Matrix[i][j]<min and visited[j]==False:
                    min=adja_Matrix[i][j]
                    pos=i
                    pos1=j
    visited[pos1]=True
    spanning_tree.append((pos+1,pos1+1,min))
print(spanning_tree)

