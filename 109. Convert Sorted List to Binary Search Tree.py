# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def convert(l):
            if not l:
                return None
            return TreeNode(l[len(l)//2], convert(l[0:len(l)//2]), convert(l[len(l)//2+1:]))
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return convert(l)