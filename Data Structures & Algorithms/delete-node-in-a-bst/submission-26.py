# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        cur = root
        parent = None
        while cur and cur.val != key: # traverse until you find node to delete if it exists
            parent = cur
            if cur.val < key:
                cur = cur.right
            else:
                cur = cur.left

        if not cur: # cur is None -> there is no key in the tree
            return root

        if not cur.right or not cur.left: # there is 0 or 1 child
            child = cur.right if cur.right else cur.left
            if parent:
                if parent.left == cur:
                    parent.left = child
                else:
                    parent.right = child
            else:
                return child
        else: # there are 2 children
            delNode = cur
            par = cur
            cur = cur.right
            while cur.left: # find smallest node from the right subtree
                par = cur
                cur = cur.left

            if par != delNode:
                par.left = cur.right
                cur.right = delNode.right    
            cur.left = delNode.left

            if parent:
                if parent.left == delNode:
                    parent.left = cur
                else:
                    parent.right = cur
            else:
                return cur

        return root

            

        