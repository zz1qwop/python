# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 내 풀이
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        pointer = head
        first = head.next
        if first != None:
            second = head.next.next
        else:
            second = None
        pointer.next = None
        
        while first != None:
            first.next = pointer
            pointer = first
            first = second
            if(second == None):
                continue
            second = second.next
            
        return pointer


# 1 재귀 구조로 뒤집기

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node: # 비어있으면 None 리턴
                return prev
            next, node.next = node.next, prev
            # 변수 next에 원래 리스트의 다음 노드를 저장해둠
            # node.next에는 이전 값을 연결 시킨다 (역순 구현)
            return reverse(next, node) # 역순 리스트인 node를 prev로 사용.
    return reverse(head)


# 2 반복 구조로 뒤집기
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
