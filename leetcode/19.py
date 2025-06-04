class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # following the 5am leetcoding guide
        # if 1 node and removing 1st return None
        if n == 1 and not head.next:
            return None

        fast = head
        slow = head
        # slow should be n-1 places behind fast
        while n > 0:
            fast = fast.next
            n -= 1
        if not fast: # means we are removing the 1st one
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
        # HELL YEAH!
        