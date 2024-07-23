# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        queue = [root]
        result = []
        d=True
        while queue:
            l = []
            nq=[]
            for n in queue :
                if n:
                    l.append(n.val)
                    nq.append(n.left)
                    nq.append(n.right)
            queue = nq
            if l:
                result.append(l if d else l[::-1])
            d = not d
        return result

    
s = Solution()
print(s.zigzagLevelOrder(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(7)))))