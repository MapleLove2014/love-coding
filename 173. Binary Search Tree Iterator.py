# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.result = []
        stack = []
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) == 0:
                break
            node = stack.pop()
            self.result.append(node.val)
            node = node.right
        
        self.total = len(result)
        self.index = 0


    def next(self) -> int:
        self.index += 1
        return self.result[self.index - 1]

    def hasNext(self) -> bool:
        return self.index < self.total


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()