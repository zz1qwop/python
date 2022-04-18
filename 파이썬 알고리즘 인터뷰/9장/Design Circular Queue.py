# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# 내 풀이
class MyCircularQueue:

    def __init__(self, k: int):
        self.circular = [-1 for _ in range(k)]
        self.front = -1
        self.rear = -1
        self.queueLen = k
        
    def enQueue(self, value: int) -> bool:
        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
        elif (self.rear + 1)%self.queueLen == self.front%self.queueLen:
            return False
        else:
            self.rear = (self.rear+1) % self.queueLen
                
        self.circular[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.front == -1 and self.rear == -1:
            return False
        
        self.circular[self.front] = -1
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front+1) % self.queueLen
        
        return True

    def Front(self) -> int:
        return self.circular[self.front]

    def Rear(self) -> int:
        return self.circular[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1 and self.rear == -1

    def isFull(self) -> bool:
        return self.front == (self.rear + 1) % self.queueLen



# 1 배열을 이용한 풀이

class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    # enQueue() : rear 포인터 이동
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    # deQueue() : front 포인터 이동
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.1[self.p2 - 1] is None else self.q[self.p2 -1]
    # rear는 마지막 원소 + 1을 가리키고 있음.

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None
