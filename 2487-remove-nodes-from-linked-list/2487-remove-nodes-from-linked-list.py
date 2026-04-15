# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        stack = []
        while curr:
            while stack and curr.val > stack[-1]:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next

        dummy = ListNode()
        curr_node = dummy
        print(stack)
        for n in stack:
            curr_node.next = ListNode(n)
            curr_node = curr_node.next
        
        return dummy.next


        

    

        