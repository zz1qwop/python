# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# 내 풀이
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(s, letters):
            if letters == None:
                output.append(s)
            else:
                for alpha in mydict[letters[0]]:
                    if len(letters) > 1:
                        dfs(s+alpha, letters[1:])
                    else:
                        dfs(s+alpha, None)
        
        mydict = { '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        output = []
        
        if not digits:
            return output
        
        for alpha in mydict[digits[0]]:
            if len(digits) == 1:
                dfs(alpha, None)
            else:
                dfs(alpha, digits[1:])
            
        return output


# 1 모든 조합 탐색
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return

            # 입력값 자릿수 단위 반복
            # index부터 digits 길이까지
            for i in range(index, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복. ex - 2는 dfs(1, a) dfs(1, b) dfs(1, c)
                for j in dic[digits[i]]:
                    dfs(i+1, path+j)

        # 예외 처리
        if not digits:
            return []

        dic = { '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = []
        dfs(0, "")

        return result