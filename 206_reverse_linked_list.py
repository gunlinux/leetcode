"""
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def walk(node: ListNode):
    print(node.val)
    if not node.next:
        return
    walk(node.next)
    print()


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        [0 -> [1 -> [ 2 -> ]
        """
        prev = None 
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev 


if __name__ == "__main__":
    root = ListNode(0)
    root.next = ListNode(1)
    root.next.next = ListNode(2)
    walk(root)

    s = Solution()
    f = s.reverseList(root)

    walk(f)
    #print()
    #print(f.val, f.next, f.next.next)
