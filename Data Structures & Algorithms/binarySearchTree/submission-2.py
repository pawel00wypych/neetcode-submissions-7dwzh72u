class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)
        else:
            new_node = TreeNode(key,val)
            cur = self.root
            parent = None
            while cur:
                parent = cur
                if new_node.key < cur.key:
                    cur = cur.left
                elif new_node.key > cur.key:
                    cur = cur.right
                elif new_node.key == cur.key:
                    cur.value = new_node.value
                    return
            if parent.key < new_node.key:
                parent.right = new_node
            else:
                parent.left = new_node

    def get(self, key: int) -> int:
        cur = self.root
        while cur and cur.key != key:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right

        if not cur:
            return -1
        else:
            return cur.value

    def getMin(self) -> int:
        cur = self.root
        parent = None
        while cur:
            parent = cur
            cur = cur.left
        if parent:
            return parent.value
        else:
            return -1 

    def getMax(self) -> int:
        cur = self.root
        parent = None
        while cur:
            parent = cur
            cur = cur.right
        if parent:
            return parent.value
        else:
            return -1 

    def remove(self, key: int) -> None:
        cur = self.root
        parent = None
        while cur and cur.key != key:
            parent = cur
            if cur.key < key:
                cur = cur.right
            else:
                cur = cur.left
        if not cur:
            return

        if not cur.left or not cur.right: #0 or 1 child
            child = cur.left if cur.left else cur.right
            if parent:
                if parent.left == cur:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child
                return
        else: # 2 children
            delNode = cur
            par = delNode
            cur = cur.right
            while cur.left: # find smallest node in right subtree
                par = cur
                cur = cur.left
            
            cur.left = delNode.left
            if par != delNode:
                par.left = cur.right
                cur.right = delNode.right
            
            if parent:
                if parent.left == delNode:
                    parent.left = cur
                else:
                    parent.right = cur
            else:
                self.root = cur
                return

    def getInorderKeys(self) -> List[int]:
        keys = []
        stack = []
        cur = self.root
        while cur or stack: #inorder traversal
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            keys.append(cur.key)
            cur = cur.right
        return keys
