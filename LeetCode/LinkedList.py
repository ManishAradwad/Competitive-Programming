# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = []
        while(head!=None):
            binary.append(str(head.val))
            head = head.next
        return (int(''.join(binary),2))