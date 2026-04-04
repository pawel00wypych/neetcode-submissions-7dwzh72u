# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {}
        for i in range(len(inorder)): # O(n) time + O(n) extra space
            inorder_dict[inorder[i]] = i

        def buildTreeHelper(pre_root_idx, ino_left_bound, ino_right_bound):
            nonlocal inorder_dict, preorder, inorder
            if ino_left_bound >= ino_right_bound:
                return None
            
            root = TreeNode(preorder[pre_root_idx])
            ino_root_idx = inorder_dict[root.val]

            l_len = ino_root_idx - ino_left_bound

            root.left = buildTreeHelper(pre_root_idx + 1, ino_left_bound, ino_root_idx)
            root.right = buildTreeHelper(pre_root_idx + l_len + 1, ino_root_idx+1, ino_right_bound)
            return root
                    
        root = buildTreeHelper(pre_root_idx = 0, 
                                ino_left_bound = 0,
                                ino_right_bound = len(inorder)
         )
        return root