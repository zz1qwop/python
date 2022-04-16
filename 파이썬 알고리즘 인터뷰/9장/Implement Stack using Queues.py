# 225. Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/

# push() 할 때 큐를 이용해 재정렬
class MyStack:

    def __init__(self):
        self.q = collections.deque()
        
    def push(self, x: int) -> None:
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

'''
deque : append(), appendleft(), pop(), popleft()
'''
