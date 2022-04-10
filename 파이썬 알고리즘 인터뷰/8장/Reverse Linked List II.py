# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 내 풀이
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        i = 1
        node = head
        left_node = right_node= reverse_left= reverse_right = None
        
        while node:
            if i == left:
                reverse_right = node
            elif i == left-1:
                left_node = node
            elif i == right:
                reverse_left = node
            elif i == right+1:
                right_node = node
            
            node = node.next
            i += 1
            
        # reverse
        reverse_left = self.reverseList(reverse_right, reverse_left, right-left+1)
        
        if left_node :   
            left_node.next = reverse_left
        reverse_right.next = right_node
        
        if left_node is None:
            return reverse_left
        else:
            return head
    
    def reverseList(self, left: ListNode, right: ListNode, count: int) -> ListNode:
        if count == 1:
            return left
        head = left
        prev = None
        for i in range(count):
            next, head.next = head.next, prev
            prev = head
            head = next
        return right


# 1 반복 구조로 노드 뒤집기
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 예외 처리
        if not head or m == n:
            return head

        root = start = ListNode(None)
        root.next = head
        # start, end 지정
        for _ in range(m-1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next
