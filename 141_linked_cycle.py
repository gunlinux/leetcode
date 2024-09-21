from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def walk_node(node: ListNode):
    t = node
    while t:
        print(t.val, ' ', end='')
        t = t.next
    print()


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return False
        slow = head
        fast = head.fast
        while (fast and fast.next and fast.next.next):
            if slow == fast:
                return True
            print(slow.val, fast.val)
            slow = slow.next
            fast = fast.next.next
        return False


if __name__ == "__main__":
    s = Solution()
    # [1,2,3,4-> None]
    node = ListNode("1")
    node.next = ListNode("2")
    node.next.next = ListNode("3")
    node.next.next.next = ListNode("4")
    walk_node(node)
    print(s.hasCycle(node))

    # [1,2,3 -> 2] 
    loop = ListNode("1")
    loop.next = ListNode("2")
    loop.next.next = ListNode("3")
    loop.next.next.next = loop.next
    print(s.hasCycle(loop))
