# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        import collections
        res = []
        q = collections.deque([root])

        while q:
            lenQ = len(q)
            temp_res = []
            for _ in range(lenQ):
                node = q.popleft()
                if node:
                    temp_res.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(temp_res)
        return res

