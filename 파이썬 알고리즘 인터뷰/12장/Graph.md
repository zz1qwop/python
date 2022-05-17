# 그래프

### 수학에서, 좀 더 구체적으로 그래프 이론에서 그래프란 객체의 일부 쌍들이 연관되어 있는 객체 집합 구조를 말한다.

<hr />

## 오일러 경로

오일러는 모든 정점이 짝수 개의 차수를 갖는다면 모든 다리를 한 번씩만 건너서 도달하는 것이 성립한다고 말했다.
모든 간선을 한 번씩 방문하는 유한 그래프를 오일러 경로라 부른다.

<hr />

## 해밀턴 경로

해밀턴 경로는 각 정점을 한 번씩 방문하는 무향 또는 유향 그래프 경로를 말한다.

- 해밀턴 경로 vs 오일러 경로
  - 해밀턴 경로 : 정점을 기준
  - 오일러 경로 : 간선을 기준
- 해밀턴 경로를 찾는 문제는 최적 알고리즘이 없는 NP-완전 문제다.

- 해밀턴 순환 : 원래의 출발점으로 돌아오는 경로
- 이중에서도 최단 거리를 찾는 문제는 외판원 문제(TSP)로 유명하다.

### 참고 : NP 복잡도

- NP는 비결정론적 튜링 기계로 다항 시간 안에 풀 수 있는 판정 문제의 집합으로, NP는 비결정론적 다항시간의 약자다.

<hr />

## 그래프 순회

그래프 순회란 그래프 탐색이라고도 불리우며 그래프의 각 정점을 방문하는 과정을 말한다.

- 그래프의 각 정점을 방문하는 그래프 순회는

  - 깊이 우선 탐색(DFS) : 주로 스택으로 구현하거나 재귀로 구현. 백트래킹을 통해 뛰어난 효용을 보인다.
  - 너비 우선 탐색(BFS) : 주로 큐로 구현, 그래프의 최단 경로를 구하는 문제 등에 사용된다.
  - 의 2가지 알고리즘이 있다.

- 그래프를 표현하는 방법에는
  - 인접 행렬
  - 인접 리스트 : 출발 노드를 키로, 도착 노드를 값으로 표현할 수 있다. 도착 노드는 리스트 형태가 된다.
    - graph = { 1: [2,3,4], 2: [5], 3: [5], 4: [], 5: [6,7], 6: [], 7: [3]} <- 딕셔너리 자료형으로 표현한 것.
  - 의 2가지 방법이 있다.

### DFS(깊이 우선 탐색)

- 재귀 구조로 구현

```
DFS(G, v)
  label v as discovered
  for all directed edges from v to w that are in G.adjacentEdges(v) do
    if vertex w is not labeled as discovered then
      recursively call DFS(G, w)
```

- 정점 v의 모든 인접 유향(Directed) 간선들을 반복.

```Python
def recursive_dfs(v, discovered=[]):
  discovered.append(v)
  for w in graph[v]:
    if w not in discovered:
      discovered = recursive_dfs(w, discovered)
  return discovered

  # [1,2,5,6,7,3,4]
```

- 스택을 이용한 반복 구조로 구현

```
DFS-iterative(G, v)
  let S be a stack
  S.push(v)
  while S is not empty do
    v = S.pop()
    if v is not labeled as discovered then
      label v as discovered
      for all edges from v to w in G.adjacentEdges(v) do
        S.push(w)
```

- 스택을 이용해 모든 인접 간선을 추출하고 다시 도착점인 정점을 스택에 삽입하는 구조이다.

```Python
def iterative_dfs(start_v):
  discovered = []
  stack = [start_v]
  while stack:
    v = stack.pop()
    if v not in discovered:
      discovered.append(v)
      for w in graph[v]:
        stack.append(w)
  return discovered
  # [1,4,3,5,7,6,2]
```

- 재귀 DFS는 사전식 순서로 방문한 데 반해 반복 DFS는 역순으로 방문했다. 이는 스택으로 구현했기 때문에 가장 마지막에 삽입된 노드부터 꺼내 반복하게 되는 일 때문이다.

### BFS(너비 우선 탐색)

- 최단 경로를 찾는 다익스트라 알고리즘 등에 매우 유용하게 쓰인다.

- 큐를 이용한 반복 구조로 구현

```
BFS(G, start_v)
  let Q be a queue
  label start_v as discovered
  Q.enqueue(start_v)
  while Q is not empty do
    v := Q.dequeue()
    if v is the goal then
      return v
    for all edges from v to w in G.adjacentEdges(v) do
      if w is not labeled as discovered then
        label w as discovered
        w.parent := v
        Q.enqueue(w)
```

```Python
def iterative_bfs(start_v):
  discovered = [start_v]
  queue = [start_v]
  while queue:
    v = queue.pop(0)
    for w in graph[v]:
      if w not in discovered:
        discovered.append(w)
        queue.append(w)
  return discovered
  # [1,2,3,4,5,6,7]
```

- 재귀 구현 불가
  - BFS는 재귀를 사용할 수 없고 큐를 이용해 구현한다.

<hr />

## 백트래킹

백트래킹은 해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되는 즉시 후보를 포기해 정답을 찾아가는 범용적인 알고리즘으로 제약 충족 문제에 특히 유용하다.

- DFS와 같은 방식으로 탐색하는 모든 방법을 뜻한다.
- DFS는 백트래킹의 골격을 이루는 알고리즘이다.
- 백트래킹은 주로 재귀로 구현한다.
- 가능성이 없는 후보를 버리는 것 : 가지치기(Pruning)

<hr />

## 제약 충족 문제

백트래킹은 가지치기를 통해 제약 충족 문제(CSP)를 최적화 한다.

- 제약 충족 문제 : 수많은 제약 조건을 충족하는 상태를 찾아내는 수학 문제.
- ex. 스도쿠, 십자말 풀이, ...
