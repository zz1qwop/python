# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/

# 내 풀이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_dict = {}
        for j in jewels:
            jewel_dict[j] = 0
            
        for s in stones:
            if s in jewel_dict:
                jewel_dict[j] += 1
                
        output = 0
        for _, v in jewel_dict.items():
            output += v
            
        return output

# 1 해시 테이블을 이용한 풀이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}
        count = 0

        # 돌의 빈도 수 계산
        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        # 보석의 빈도 수 계산
        for char in jewels:
            if char in freqs:
                count += freqs[char]

        return count

# 2 defaultdict 를 이용한 비교 생략
import collections
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs= collections.defaultdict(int)
        count = 0

        for char in stones:
            freqs[char] += 1

        for char in jewels:
            count += freqs[char]

        return count
        # 키가 존재하는지 여부를 매번 판별할 필요가 없어졌다.


# 3 Counter로 계산 생략
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones) # 돌 빈도 수 계산
        count = 0

        for char in jewels:
            count += freqs[char]

        return count
        # Counter는 존재하지 않는 키의 경우 KeyError를 발생하는 게 아니라 0을 출력해줌.

# 4 파이썬다운 방식
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)

'''
[s for s in S] : ['a', 'A', 'A', 'b', 'b', 'b', 'b']
[s in J for s in S] : [True, True, True, False, False, False, False]
sum([s in J for s in S]) : 결과는 True의 개수로 3이 된다.
'''