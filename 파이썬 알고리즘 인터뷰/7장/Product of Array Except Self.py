# 238. Product of Array Except Self

# 내 풀이 1 - Time Limit Exceeded가 발생
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        
        for i in range(len(nums)):
            left, right = 0, len(nums)-1
            result = 1
            
            if nums[i] != 0 and 0 in nums:
                results.append(0)
                continue
            
            while left<i or right>i:
                if left<i:
                    result *= nums[left]
                    left += 1
                if right>i:
                    result *= nums[right]
                    right -= 1
            
            results.append(result)
        return results

# 내 풀이 2
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        left = []
        right = []
        
        # left
        for i in range(len(nums)):

            if i == 0:
                left.append(1)
            else:
                left.append(left[i-1] * nums[i-1])
                
        # right
        for i in range(len(nums)):
            
            if i == 0:
                right.append(1)
            else:
                right.append(right[i-1] * nums[len(nums)-i])
            
            
        # product
        for i in range(len(nums)):
            results.append(left[i] * right[len(nums)-i-1])
            
        return results


# 1 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums)-1, 0 -1, -1):
            out[i] = out[i] * p
            p  = p * nums[i]
        return out

    # 기존 out 변수를 활용했으므로 공간 복잡도 O(1)에 가능.
    # for문에서 (len(nums)-1, 0 - 1, -1)로 인덱스를 거꾸로 가져왔기 때문에 코드가 간결
