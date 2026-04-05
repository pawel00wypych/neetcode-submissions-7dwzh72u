# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = dict()
        for i in range(len(inorder)):
            inorder_dict[inorder[i]] = i

        def buildTreeHelper(pre_idx, left_bound, right_bound):
            nonlocal inorder_dict, inorder, preorder
            if left_bound >= right_bound:
                return None

            root = TreeNode(preorder[pre_idx])
            ino_idx = inorder_dict[root.val]

            len_left = ino_idx - left_bound
            len_right = right_bound - ino_idx

            root.left = buildTreeHelper(pre_idx + 1, left_bound, ino_idx)
            root.right = buildTreeHelper(pre_idx + len_left + 1, ino_idx+1, right_bound)
            return root
        root = buildTreeHelper(0, 0, len(inorder))
        return root