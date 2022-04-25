
# 데크
데크 : 데크는 더블 엔디드 큐(Double-Ended Queue)의 줄임말로, 글자 그대로 양쪽 끝을 모두
          추출할 수 있는, 큐를 일반화한 형태의 추상 자료형(ADT)이다.

- 데크는 양쪽에서 삭제와 삽입을 모두 처리할 수 있으며, 스택과 큐의 특징을 모두 갖고 있다.
- ADT의 구현은 배열이나 연결 리스트 모두 가능하지만, 이중 연결 리스트로 구현하는 편이 가장 잘 어울린다.
- 이중 연결 리스트로 구현 시 양쪽으로 head와 tail이라는 두 포인터를 갖고 있다가
  새 아이템이 추가될 때마다 앞쪽 또는 뒤쪽으로 연결시켜 준다. 연결 후에는 포인터를 이동한다.

- 파이썬은 데크 자료형을 collections 모듈에서 deque라는 이름으로 지원한다.

import collections
d = collections.deque()


# 우선순위 큐
우선순위 큐 : 큐 또는 스택과 같은 추상 자료형과 유사하지만 추가로 각 요소의 '우선순위'와 연관되어 있다.

- 우선순위 큐는 어떠한 특정 조건에 따라 우선순위가 가장 높은 요소가 추출되는 자료형이다.
- ex. 최댓값을 추출하는 우선순위 큐
- 정렬 알고리즘을 사용하면 우선순위 큐를 만들 수 있다.
