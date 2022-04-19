# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

# 1 스택 값 비교

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer

# stack에는 temperatures의 인덱스를 넣음.
# 현재의 인덱스를 스택에 쌓아두고 상승하는 시점에서 현재 온도와 스택에서 쌓아둔 인덱스 지점의 온도 차이를 비교
# 현재 온도가 더 높다면 스택의 값을 pop하고 스택의 값(인덱스)과 현재 인덱스의 차이를 입력한다.
# 스택에 인덱스를 저장해뒀기 때문에 차이를 입력할 때 answer[index]로 입력 가능.
# answer의 요소들은 디폴트로 0을 가지고 있음.
