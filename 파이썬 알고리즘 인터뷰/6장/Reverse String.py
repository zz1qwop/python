# 344. Reverse String
"""
# 1 투 포인터를 이용한 스왑
def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
"""

# 2 파이썬다운 방식
def reverseStrig(self, s: List[str]) -> None:
    s.reverse()


"""
s[:] = s[::-1]
-> 공간 복잡도에 문제가 있을 시 사용
"""
