# 125. Valid Palindrome

"""
# 1 리스트로 변환
def isPlaindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
                strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs)>1:
        if strs.pop(0) != strs.pop():
            return False

    return True
"""
"""
# 2 데크 자료형을 이용한 최적화
def isPlaindrome(self, s: str) -> bool:
    # 자료형을 데크로 선언
    strs: Deque = collections.deque()
    
    for char in s:
        if char.isalnum():
                strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs)>1:
        if strs.popleft() != strs.pop():
            return False

    return True
"""

# 3 슬라이싱 사용
def isPlaindrome(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::1] # 슬라이싱
