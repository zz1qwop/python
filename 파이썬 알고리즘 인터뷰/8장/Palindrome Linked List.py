# 234. Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 내 풀이
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        value = []
        while head != None:
            value.append(head.val)
            head = head.next
            
        while len(value) > 1:
            if value.pop(0) != value.pop():
                return False
            
        return True

# 1 리스트 변환
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True


# 2 데크를 이용한 최적화
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 데크 자료형 선언
        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

# 동적 배열로 구성된 리스트는 첫 번재 값을 가져오면 모든 값이 한 칸씩 시프팅 되며, 시간 복잡도 O(n)이 발생.
# Deque는 이중 연결 리스트 구조로 양쪽 방향 모두 추출하는 데 시간 복잡도 O(1)에 실행된다.


# 4 런너를 이용한 우아한 풀이
'''
Runner : 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법.
                한 포인터가 다른 포인터보다 앞서게 하여 병합 지점이나 중간 위치, 길이 등을 판별할 때 유용하게 사용한다.
                빠른 런너가 연결 리스트 끝에 도달하면, 느린 런너는 연결 리스트의 중간 지점을 가리킨다.
'''

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        # 입력 값이 홀수일때는 한 칸 더 이동하여 중앙 값 벗어나기
        # fast는 2칸 씩 이동. 1 -> 2 -> 3-> 4 -> 5 -> 6 -> 여기에 도달해서 짝수일 경우 None
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev # 또는 return not slow

'''
다중 할당 : 2개 이상의 값을 2개 이상의 변수에 동시에 할당하는 것.
ex. rev = 1, slow = 2 -> 3
rev, rev.next, slow = slow, rev, slow.next
이 경우 rev = 2->3, rev.next = 1, slow = 3 / 최종적으로 rev = 2->1.
다중 할당을 하게 되면 이 같은 작업이 동시에 일어나 중간 과정 없이 한 번의 트랜잭션으로 끝나게 된다.

cf. rev, rev.next = slow, rev
     slow = slow.next
첫 줄 실행 결과 : rev = 2->3, rev.next = 1. rev = 2->1
여기서 rev = slow를 했으므로 동일한 참조가 되어 slow = 2->1이 되어버린다.
결국 두 번째 줄 실행 결과 slow = 1이 되어 앞선 다중 할당과 다른 결과가 된다.
'''
