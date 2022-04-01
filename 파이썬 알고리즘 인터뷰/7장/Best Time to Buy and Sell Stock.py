# 121. Best Time to Buy and Sell Stock

# 내 풀이 1 - Time Limit Exceeded 발생
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for i in range(len(prices)-1, 0 - 1, -1):
            for j in range(i):
                if prices[i] > prices[j]:
                    if prices[i] - prices[j] > maximum:
                        maximum = prices[i] - prices[j]
        
        return maximum

# 내 풀이 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        low = [0, prices[0]]
        high = [0, prices[0]]
        
        for i in range(1, len(prices)):
            if prices[i] < low[1]:
                low = [i, prices[i]]
                if low[0] > high[0]:
                    high = [0, 0]
                elif low[0] < high[0]:
                    if maximum < high[1] - low[1]:
                        maximum = high[1] - low[1]
            elif prices[i] > high[1]:
                high = [i, prices[i]]
                if maximum < high[1] - low[1]:
                    maximum = high[1] - low[1]
        
        return maximum
    # 너무 복잡하게 풀었음 -> if문 구조도 깊게 들어감.


# 1 브루트 포스로 계산
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)

        return max_price


# 2 저점과 현재 값과의 차이 계산
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price-min-price)

        return profit
