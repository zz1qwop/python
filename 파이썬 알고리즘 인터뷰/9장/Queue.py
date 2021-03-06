# Queue

- 큐는 시퀀스의 한쪽 끝에는 엔티티를 추가하고, 다른 반대쪽 끝에는 제거할 수 있는 엔티티 컬렉션이다.
- FIFO (First-In-First-Out)
- Deque, Priority Queue 같은 변형들은 여러 분야에서 유용하게 쓰임
- 너비 우선 탐색(Breadth-First Search (BFS)), 캐시 등을 구현할 때 널리 사용
- 파이썬의 queue 모듈 : 자료구조로서의 큐보다는 동기화 기능에 집중된 모듈
- 파이썬의 리스트는 큐의 모든 연산을 지원
- 좀 더 나은 성능을 위해 양방향 삽입, 삭제가 모두 O(1)에 가능한 데크를 사용하는 편이 좋음.
