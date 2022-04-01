# 561. Array Partition 1

# 내 풀이
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for i in range(0,len(nums)-1,2):
            sum += min(nums[i], nums[i+1])
            
        return sum

# 1 오름차순 풀이
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum

# 2 짝수 번째 값 계산
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            # 짝수 번째 값의 합 계산 - min을 하지 않아도 짝수 번째 값이 항상 작은 걸 알 수 있다.
            if i % 2 == 0:
                sum += n

        return sum

# 3 파이썬다운 방식 - 슬라이싱 사용
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
    
