# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# 1 슬라이딩 윈도우와 투 포인터로 사이즈 조절
def lengthOfLongestSubstring(self, s:str) -> int:
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        # 이미 등장했던 문자라면 'start' 위치 갱신
        # 이미 등장했어도 슬라이딩 윈도우의 바깥에 있는 문자는 무시해야 한다.
        if char in used and start <= used[char]:
            start = used[char] + 1
        else: # 최대 부분 문자열 길이 갱신
            max_length = max(max_length, index - start + 1)

        # 현재 문자의 위치 삽입
        used[char] = index

    return max_length

'''
슬라이딩 윈도우로 한 칸씩 우측으로 이동하며 윈도우 내의 문자가 중복이 없도록
투 포인터로 윈도우 사이즈를 조절한다.

'''