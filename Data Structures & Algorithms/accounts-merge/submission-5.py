class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        adj = defaultdict(list)

        for account in accounts:
            for i in range(2, len(account)):
                em1 = account[i]
                em2 = account[i-1]
                adj[em1].append(em2)
                adj[em2].append(em1)
        
        emailToGroup = defaultdict(list)

        visits = set()

        def dfs(node, i):
            visits.add(node)
            emailToGroup[i].append(node)
            for nei in adj[node]:
                if nei not in visits:
                    dfs(nei, i)
        
        for i, emails in enumerate(accounts):
            for email in emails[1:]:
                if email not in visits:
                    dfs(email, i)
        
        res = []

        for key, val in emailToGroup.items():
            
            name = accounts[key][0]
            res.append([name] + sorted(val))
    
        return res



        