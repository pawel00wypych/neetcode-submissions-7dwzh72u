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
        while cur and cur.val != key:
            parent = cur
            if cur.val < key:
                cur = cur.right
            else:
                cur = cur.left

        if not cur: #there was no key in the tree
            return root

        if not cur.right or not cur.left: # 0 or 1 child
            child = cur.left if cur.left else cur.right
            if parent:
                if parent.left == cur:
                    parent.left = child
                else:
                    parent.right = child
            else:
                return child
        else: # 2 children
            delNode = cur
            cur = cur.right
            par = delNode
            while cur.left: # find smallest node in right subtree
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