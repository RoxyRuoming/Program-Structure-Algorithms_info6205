# Definition for a binary tree node.
# 1. Minimum Depth of Binary TreeLinks to an external site
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            if not node.left:
                return 1 + dfs(node.right)
            elif not node.right:
                return 1 + dfs(node.left)
            
            return 1 + min(dfs(node.left), dfs(node.right))
        # I should return the final res
        return dfs(root)

#2 Count Complete Tree NodesLinks to an external site
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0
            return 1 + dfs(node.left) + dfs(node.right)

        return dfs(root)

#3 Find Largest Value in Each Tree Row
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            cur_size = len(q)
            cur_max = float('-inf')
            for i in range(cur_size):
                pop = q.popleft()
                cur_max = max(cur_max, pop.val)
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
            res.append(cur_max)

        return res

#4 Leaf-Similar Trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, leaf):
            if not root:
                return
            if not (root.left or root.right):
                leaf.append(root.val)
            dfs(root.left, leaf)
            dfs(root.right, leaf)

        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        return leaf1 == leaf2
#5 Deepest Leaves Sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        q = collections.deque()
        q.append(root)
        while q:
            leavesSum = 0
            for i in range(len(q)):
                node = q.popleft()
                leavesSum += node.val
                for child in [node.left, node.right]:
                    if child: q.append(child)
        return leavesSum
#6 Find Leaves of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(node):
            if not node: return None
            if not(node.left or node.right):
                res[-1].append(node.val)
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node

        while root:
            res.append([])
            root = dfs(root) #update root tree
        return res


