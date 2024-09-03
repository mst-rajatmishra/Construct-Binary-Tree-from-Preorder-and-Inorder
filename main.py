class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        # Create a dictionary to store the index of each value in inorder
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        
        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            
            # The first element in preorder is the root
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # Find the index of the root in inorder
            root_index = inorder_index[root_val]
            
            # Number of elements in the left subtree
            left_size = root_index - in_start
            
            # Recursively build the left and right subtrees
            root.left = build(pre_start + 1, pre_start + left_size, in_start, root_index - 1)
            root.right = build(pre_start + left_size + 1, pre_end, root_index + 1, in_end)
            
            return root
        
        # Start building the tree
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
