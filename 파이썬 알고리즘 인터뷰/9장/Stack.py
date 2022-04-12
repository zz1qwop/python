# Stack

Stack : LIFO(Last-In-First-Out)

- 파이썬은 스택 자료형을 별도로 제공하지는 않지만 , 리스트가 사실상 스택의 모든 연산을 지원
- 다만 리스트는 동적 배열로 구현되어 있어 큐의 연산을 수행하기에는 효율적이지 않음
- Deque를 사용해야 좋은 성능을 낼 수 있음

- push() : 요소를 컬렉션에 추가
- pop() : 아직 제거되지 않은 가장 최근에 삽입된 요소를 제거

- 스택은 콜 스택이라 하여 컴퓨터 프로그램의 서브루틴에 대한 정보를 저장하는 자료구조에도 널리 활용.
- 스택 버퍼 오버플로 : 꽉 찬 스택에 요소를 삽입하고자 할 때 발생하는 에러


# 연결 리스트를 이용한 스택 ADT 구현

class Node: # 연결 리스트를 담을 클래스
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)
        # 가장 마지막 값을 next로 지정, 포인터인 last는 가장 마지막으로 이동.

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item
        # 가장 마지막 아이템을 꺼내고 last 포인터를 한 칸 앞으로 전진.
