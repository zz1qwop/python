# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

# 01 DFS로 그래프 탐색
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or \
              j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
                return

            grid[i][j] = 0
            # 동서남북 탐색
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
        return count

'''
중첩 함수
: 함수 내에 위치한 또 다른 함수. 부모 함수의 변수를 자유롭게 읽을 수 있다.
  가변 객체인 경우 append(), pop() 등 여러 연산으로 조작도 가능하다.
  재할당(=)이 일어날 경우 참조 ID가 변경되어 별도의 로컬 변수로 선언된다.

def outer_function(t: str):
    text: str = t
    print(id(text), text)

    def inner_function1():
        text = 'World!'
        print(id(text), text)

    def inner_function2():
        print(id(text), text)

    inner_function1()
    inner_function2()

outer_function('Hello!')

--- result ---
4599...144 Hello!
4599...288 World!
4599...144 Hello!

- 중첩 함수에서 재할당된 값은 부모 함수에서 반영되지 않는다.
'''