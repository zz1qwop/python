# 819. Most Common Word

# 1 리스트 컴프리헨션, Counter 객체 사용
def mostCommon Word(self, paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split()
                     if word not in banned]

    counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
    return counts.most_common(1)[0][0]

'''
- 리스트 내포 : for문과 if문을 한 라인에 작성
[표현식 for 항목 in 반복가능객체 if 조건문]
ex. [x*x for x in array]

- 정규 표현식 : 문자열을 처리할 때 사용하는 기법. 정규식이라고도 함.
    - 문자 클래스 [ ] : [ ] 사이의 문자들과 매치
    - ^ : not. [^0-9]는 숫자 아닌 문자만 매치
    - 자주 사용하는 문자 클래스
        - \d : 숫자와 매치
        - \D : 숫자가 아닌 것과 매치
        - \s : whitespace 문자와 매치
        - \S : whitespace 문자가 아닌 것과 매치
        - \w : 문자 + 숫자와 매치, [a-zA-Z0-9_]
        - \W : 문자 + 숫자가 아닌 문자와 매치
    - Dot(.) : \n을 제외한 모든 문자와 매치. [ ] 내에 사용 시 문자 . 그대로를 의미
- 파이썬에서는 정규 표현식을 지원하기 위해 re 모듈을 제공
- sub 메서드를 사용하면 정규식과 매치되는 부분을 다른 문자로 쉽게 바꿀 수 있음

참고 : https://wikidocs.net/1669
'''
