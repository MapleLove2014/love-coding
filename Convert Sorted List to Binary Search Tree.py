#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return '{}->{}->{}'.format(str(self.val), self.left, self.right)
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        count = 0
        node = head
        while node:
            count += 1
            node = node.next

        def makeTree(head, count):
            if count <= 0 or not head:
                return None
            if count == 1:
                return TreeNode(head.val)
            mid = count // 2

            move = 0
            node = head
            while node and move < mid:
                move += 1
                node = node.next
            return TreeNode(node.val, makeTree(head if move > 0 else None, mid), makeTree(node.next, count - mid - 1))
            
        return makeTree(head, count)

s = Solution()
print(s.sortedListToBST(ListNode(1, ListNode(2, ListNode(3)))))
print(s.sortedListToBST(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))

        


