# 328. Odd Even Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 내 풀이
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head
        
        p = head
        even, even_p = head.next, head.next
        
        while True:
            head.next, even.next = head.next.next, even.next.next
            head, even = head.next, even.next
            if even is None or even.next is None:
                break
            
        head.next = even_p
        return p


# 1 반복 구조로 홀짝 노드 처리
# odd, even, even_head 등의 변수들은 n의 크기에 관계 없이 항상 일정하게 사용 -> 공간 복잡도 O(1) 만족.
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 예외 처리
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head
        return head
    
