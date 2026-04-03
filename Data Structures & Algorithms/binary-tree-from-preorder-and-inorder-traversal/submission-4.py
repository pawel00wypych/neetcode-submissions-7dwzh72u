# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # we must do this by recursively dividing the tree to left and right subtrees
        # we take root val from preorder first element
        # we look for that val in inorder list, when we find it we take index of inorder root position
        # we divide inorder into two subarrays:
        # left [0,ino_root_indx-1] and right [ino_root_indx+1, len(arr)]
        # we divide preorder array into two subarrays:
        # left subarray = [1,len(left_sub)], right sub = [len(left_sub)+1, len(right_sub)]
        # from root we create node and recursively repeat that process assigning root.left to 
        # left recursion call, and root.right to right recursion call
        # we stop when arr length is <= 1 
        if len(preorder) < 1:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        ino_root_indx = 0
        while root.val != inorder[ino_root_indx]:
            ino_root_indx += 1

        len_of_left_subarr = len(inorder[0:ino_root_indx])
        len_of_right_subarr = len(inorder[ino_root_indx+1:])
        
        root.left = self.buildTree(preorder[1:len_of_left_subarr+1], inorder[0:ino_root_indx])
        root.right = self.buildTree(preorder[len_of_left_subarr+1:], inorder[ino_root_indx+1:])
        return root
