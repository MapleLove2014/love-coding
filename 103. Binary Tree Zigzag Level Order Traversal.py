# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        result = []
        left2right = True
        while len(queue) > 0:
            orderQueue = queue if left2right else reversed(queue)
            result.append([node.val for node in orderQueue])
            left2right = not left2right
            thisQueue = []
            for node in queue:
                if node.left:
                    thisQueue.append(node.left)
                if node.right:
                    thisQueue.append(node.right)
            queue = thisQueue
        return result
