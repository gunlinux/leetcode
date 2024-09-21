from listnode import LList, ListNode
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return
        root = head
        prev = head
        cur = head.next

        while cur:
            if prev.val == cur.val:
                prev.next = cur.next
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        return root


if __name__ == "__main__":
    sorted_list: LList = LList(1, 1, 2)  # , 3, 3)

    s = Solution()
    t = s.deleteDuplicates(head=sorted_list.root)
    for i in t:
        print(f"{i}, ", end="")
