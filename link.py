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


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


if __name__ == "__main__":
    root = ListNode(0)
    root.next = ListNode(1)
    root.next.next = ListNode(2)
    walk(root)
