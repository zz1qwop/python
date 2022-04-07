# 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 내 풀이
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        answer = result
        while l1 is not None or l2 is not None:
            if l1 != None:
                result.val += l1.val
                l1 = l1.next
            if l2 != None:
                result.val += l2.val
                l2 = l2.next
            if result.val > 9:
                result.next = ListNode(1)
                result.val -= 10
                result = result.next
            elif not (l1 is None and l2 is None) :
                result.next = ListNode()
                result = result.next

        return answer

# 1자료형 반환
class Solution:
    # 연결 리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result:str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node

    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        # = int(''.join(map(str,a))) 로도 바꿀 수 있다.
        # = functools.reduce(lambda x, y: 10*x + y, a, 0) 으로 한 번에 숫자형으로 바로 변경 가능.

        # 최종 계산 결과 연결 리스트 변환
        return self.toReversedLinkedList(str(resultStr))


# 2 전가산기 구현
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry), 10)
            head.next = ListNode(val)
            head = head.next

        return root.next

'''
입력값 A, B, 이전의 자리올림수(Carry in) 3가지 입력으로 합과 다음 자리올림수 여부를 결정한다.
연산 결과로 나머지를 취하고 몫은 자리올림수 형태로 올린다.
carry, val = divmod(sum+carry, 10)
- divmod() : 파이썬 내장 함수로 몫과 나머지로 구성된 튜플을 리턴한다.
- (a//b, a%b)와 동일한 결과를 출력한다. 
'''
