def count_components(G):
    V = len(G)
    visited = [False] * V
    count = 0
    def dfs(v):
        visited[v] = True
        for w in range(v):
            if G[v][w] and not visited[w]:
                dfs(w)
    for v in range(v):
        if not visited[v]:
           count +=1
           dfs(v)
    return count
G = [[0, 1, 0, 1],
     [1, 0, 1, 0],
     [0, 1, 0, 1],
     [1, 0, 1, 0]]
count = count_components(G)
print(count)