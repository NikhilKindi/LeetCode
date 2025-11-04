class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node, adj, vis):
            vis[node]=1
            for i in adj[node]:
                if vis[i]!=1:
                    dfs(i, adj, vis)
        n= len(isConnected)
        adj=[[] for _ in range(n)]
        vis=[0 for _ in range(n)]
        c=0

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    adj[i].append(j)
                    adj[j].append(i)

        for i in range(n):
            if vis[i]!=1:
                c+=1
                dfs(i, adj, vis)
        
        return c
        
        