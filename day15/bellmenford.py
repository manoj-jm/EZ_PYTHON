def bellmanford(V,edges,S):
    d=[float('inf')]*V
    d[S]=0
    for _ in range(V - 1):
        for u,v,wt in edges:
            if d[u]!=float('inf') and d[u]+wt<d[v]:
                d[v] = d[u] + wt

# # Check for negative-weight cycles.
#     for u, v, wt in edges:
#         if d[u]!=float('inf') and d[u]+wt<d[v]:
#             return [-1]

    return d
if __name__ == "__main__":
    V = 6
    S = 0
    edges = [
        [3, 2, 6],
        [5, 3, 1],
        [0, 1, 5],
        [1, 5, -3],
        [1, 2, -2],
        [3, 4, -2],
        [2, 4, 3]
    ]
    d=bellmanford(V,edges,S)
    #print(" ".join(map(str,d)))
    print(d)