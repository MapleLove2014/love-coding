
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def c(node, fd):
            if not node:
                return None
            cn = Node(node.val)
            fd[node.val] = cn
            cn.neighbors = [c(n, fd) if n.val not in fd else fd[n.val] for n in node.neighbors]
            return cn
        return c(node, {})
        
            

        