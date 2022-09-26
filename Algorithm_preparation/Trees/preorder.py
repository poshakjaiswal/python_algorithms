from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def preorder(self, root: TreeNode, accumulator: List) -> List[int]:

        if root == None:
            return accumulator
        print(root.val)
        accumulator.append(root.val)

        if root.left != None:
            self.preorderTraversal(root.left, accumulator)

        if root.right != None:
            self.preorderTraversal(root.right, accumulator)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root == None:
            return []
        predorderT = self.preorder(self, root, [])

        return predorderT