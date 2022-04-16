# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/

# 내 풀이
class MyQueue:

    def __init__(self):
        self.stackA = []
        self.stackB = []
        

    def push(self, x: int) -> None:
        if len(self.stackA) != 0:
            for _ in range(len(self.stackA)):
                self.stackB.append(self.stackA.pop())
            self.stackA.append(x)
            for _ in range(len(self.stackB)):
                self.stackA.append(self.stackB.pop())
        else:
            self.stackA.append(x)

    def pop(self) -> int:
        return self.stackA.pop()

    def peek(self) -> int:
        return self.stackA[len(self.stackA)-1]

    def empty(self) -> bool:
        return len(self.stackA) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# 스택 2개 사용
class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
    # input에 있는 것을 output에 입력 <- stack의 역순으로 입력되기 때문에 FIFO로 pop 가능하게 함.
    # output이 비워지고 나서야 input에 있는 걸 새로 가져온다 <- 그래야 순서 안 꼬임
    
    def empty(self) -> bool:
        return self.input == [] and self.ouput == []
