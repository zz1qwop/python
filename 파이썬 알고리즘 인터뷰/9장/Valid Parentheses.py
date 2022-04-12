# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/


# 1 스택 일치 여부 판별

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{'
            ']': '['
        }

        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0

'''
(, {, [는 스택에 Push, ), }, ]를 만날 때 스택에서 Pop한 결과가 매핑 테이블 결과와 매칭되는지 확인.
if char not in table : (, {, [인 경우 스택에 push
elif not stack or table[char] != stack.pop() : ), }, ]인 경우 스택이 비어있거나 pop한 결과와 매칭이 안 될 경우
return len(stack) == 0 : ex. "("만 입력되었을 때는 len(stack)이 1인 채로 끝나므로 False가 리턴.
'''
