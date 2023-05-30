# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr=ListNode()
        x=curr
        while head:
            if head.val== val and head.next is None:
                curr.next=head.next
                curr=curr.next
                head=head.next
                break
            if head.val==val:
                # print(1)
                head=head.next
            else:
                # print(2)
                curr.next=head
                curr=curr.next
                head=head.next
                continue
        return x.next
        