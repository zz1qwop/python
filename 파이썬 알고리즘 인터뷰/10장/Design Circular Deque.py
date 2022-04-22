# 641. Design Circular Deque
# https://leetcode.com/problems/design-circular-deque/


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


# 내 풀이

class MyCircularDeque:

    def __init__(self, k: int):
        self.maxSize = k
        self.circular = [None] * k
        self.head, self.tail = None, None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.head == None:
            self.circular[0] = value
            self.head, self.tail = 0, 0
            return True
        
        self.circular[(self.head - 1) % self.maxSize] = value
        self.head = (self.head-1)%self.maxSize
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.tail == None:
            self.circular[0] = value
            self.head, self.tail = 0, 0
            return True
        
        self.circular[(self.tail + 1) % self.maxSize] = value
        self.tail = (self.tail+1)%self.maxSize
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head, self.tail = None, None
            return True
        
        self.head = (self.head+1)%self.maxSize
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head, self.tail = None, None
            return True
        
        self.tail = (self.tail-1)%self.maxSize
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.circular[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.circular[self.tail]
        

    def isEmpty(self) -> bool:
        if self.head == None and self.tail == None:
            return True
        return False

    def isFull(self) -> bool:
        if self.head == None or self.tail == None:
            return False
        elif self.head == (self.tail + 1) % self.maxSize:
            return True
        return False


# 1 이중 연결 리스트를 이용한 데크 구현

class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head # head와 tail 연결

    # 이중 연결 리스트에 신규 노드 삽입
    def _add(self, node: ListNode, new: ListNode):
        n  = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new
    # node와 node.right 사이에 new를 끼워넣는다.

    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node
        
    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k

