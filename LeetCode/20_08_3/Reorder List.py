# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        def searchNode(n, Node):
            for _ in range(n):
                Node = Node.next
            return Node

        def connectNode(oldNode, newNode):
            temp = oldNode.next
            oldNode.next = newNode
            newNode.next = temp.next

        tail = head
        length = 0
        while True:
            if not tail:
                break
            tail = tail.next
            length += 1

        for i in range(length//2):
            connectNode(searchNode(i, head), searchNode(length - i, head))



a = Solution()
print(a.reorderList())


