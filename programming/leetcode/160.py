# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    # following the 5 am leetcoding guide 
    # connect both lists a->b and b->a, iterate through both, 
    # first time they meet is when they intersect, We won. 
    # we can pretend the lists are connected if we start iterating over listA when listB ends and listB when listA ends
        ptr_a = headA
        ptr_b = headB
        flag_a, flag_b = False, False

        while ptr_a and ptr_b:
            if ptr_a == ptr_b:
                return ptr_a
            if not ptr_a.next and not flag_a:
                ptr_a = headB
                flag_a = True
            elif not ptr_a.next and flag_a:
                return None # repetition
            else:
                ptr_a = ptr_a.next


            if not ptr_b.next:
                ptr_b = headA
                flag_b = True
            elif not ptr_b.next and flag_b:
                return None # repetition
            else:
                ptr_b = ptr_b.next

        return None
