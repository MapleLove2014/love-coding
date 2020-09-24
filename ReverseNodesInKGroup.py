# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '{}->{}'.format(self.val, self.next)
class Solution:
    def reverseKGroup(self, head: ListNode, k: int):
        result = None
        resultTail = None
        nextResult = None
        nextResultTail = None
        # the number of nodes already reversed in this group
        count = 0
        node = head
        while node:
            nextNode = node.next
            if count < k:
                # first node in this group
                # which is also the last node after reversing
                if not nextResult:
                    nextResultTail = node
                    nextResult = node
                    nextResultTail.next = None
                # other nodes in this group
                # just do the reversing with previous half-reversed nodes
                else:
                    nextResultTemp = nextResult
                    nextResult = node
                    nextResult.next = nextResultTemp
                count += 1
            # already reversed the whole group
            # concat the reversed group whith all the previous reversed groups
            if count == k:
                # this is the first reversed group
                if not result:
                    result = nextResult
                else:
                    resultTail.next = nextResult
                resultTail = nextResultTail
                nextResult = None
                nextResultTail = None
                count = 0
            node = nextNode
        # reverse the half reversed group
        node = nextResult
        nextResult = None
        while count > 0:
            nextNode = node.next
            if not nextResult:
                nextResult = node
                node.next = None
            else:
                nextResultTemp = nextResult
                nextResult = node
                nextResult.next = nextResultTemp
            count -= 1
            node = nextNode
        resultTail.next = nextResult
        return result

s = Solution()

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))

result = s.reverseKGroup(head, 3)
print(result)
