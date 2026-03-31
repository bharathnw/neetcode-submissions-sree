class TreeNode:
    def __init__(self, key:int, val:int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)
            return
        curr = self.root
        while curr:
            if key < curr.key:
                if curr.left is None:
                    curr.left = TreeNode(key, val)
                    return
                curr = curr.left
                
            elif key > curr.key:
                if curr.right is None:
                    curr.right = TreeNode(key, val)
                    return
                curr = curr.right
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root
        while curr != None:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1



    def getMin(self) -> int:
        curr = self.root
        if not curr:
            return -1
        while curr and curr.left:
            curr = curr.left
        return curr.val
        
    def findMin(self, root) -> int:
        curr = root
        if not curr:
            return None
        while curr and curr.left:
            curr = curr.left
        return curr

    def getMax(self) -> int:
        curr = self.root
        if not curr:
            return -1
        while curr and curr.right:
            curr = curr.right
        return curr.val


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    # Returns the new root of the subtree after removing the key
    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if curr == None:
            return None

        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.left == None:
                # Replace curr with right child
                return curr.right
            elif curr.right == None:
                # Replace curr with left child
                return curr.left
            else:
                # Swap curr with inorder successor
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr


    def getInorderKeys(self) -> List[int]:
        arr = []
        def helper(node):
            if node is not None:
                helper(node.left)
                arr.append(node.key)
                helper(node.right)

        helper(self.root)
        return arr



