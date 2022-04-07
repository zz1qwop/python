# 24. Swap Nodes in Pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 내 풀이 1 - Time Limit Exceeded
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        result = head.next
        
        while head:
            if head.next is None:
                break
            head.next, head.next.next = head.next.next, head
            head = head.next
            
        return result

# 내 풀이 2 - 재귀를 사용
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        first , second = head, head.next
        result = second
        
        second.next, first.next = first, second.next # swap
        first.next = Solution.swapPairs(self, first.next)

        return result


# 1 값만 교환
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur and cur.next:
            # 값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head


# 2 반복 구조로 스왑
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록 할당
            prev.next = b

            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        return root.next


# 3 재귀 구조로 스왑
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴 받음
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head

# p 변수는 하나만 사용하고 head를 바로 리턴할 수 있어 공간 복잡도가 낮음.
