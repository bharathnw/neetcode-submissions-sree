# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ''

        def dfs(node):
            if not node:
                return 'Nope'
            
            val = ','+str(node.val)
            right = ',' +  dfs(node.right)
            left = ',' + dfs(node.left)
            return val + right + left
        
        return dfs(root)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '':
            return None

        tokens = data.split(',')
        tokens = [t for t in tokens if t != '']

        index = [0]
        
        def dfs():
            if index[0] == len(tokens):
                return None
            
            val = tokens[index[0]]
            index[0] += 1

            if val == 'Nope':
                return None
            node = TreeNode(val)
            node.right = dfs()
            node.left = dfs()
            return node
        return dfs()
            