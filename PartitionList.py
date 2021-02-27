# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val) + ('' if not self.next else '->' + str(self.next) )
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        
        result = ListNode()
        result.next = head
        pre = result

        node = head
        nodePre = None
        overX = False
        while node:
            if not overX:
                if node.val < x:
                    pre.next = node
                    pre = pre.next
                elif node.val >= x:
                    overX = True
                    
                nodePre = node
                node = node.next
            else:
                if node.val < x:
                    nodeNext = node.next
                    # 续上结果链表
                    preNext = pre.next
                    pre.next = node
                    pre = node
                    node.next = preNext
                    if nodePre:
                        nodePre.next = nodeNext
                    node = nodeNext
                else:
                    nodePre = node
                    node = node.next
                
        return result.next

s = Solution()
print(s.partition(ListNode(1, ListNode(1)), 0))
print(s.partition(ListNode(2, ListNode(1)), 2))
print(s.partition(ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 3))







