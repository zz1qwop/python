# 49. Group Anagrams

# 1 정렬하여 딕셔너리에 추가
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

'''
sorted()는 key= 옵션을 지정해 정렬을 위한 키 또는 함수를 별도 지정 가능

ex)
c = ['ccc', 'aaaa', 'd', 'bb']
sorted(c, key=len)
-> ['d', 'bb', 'ccc', 'aaaa']

a=['cde', 'cfc', 'abc']
def fn(s):
    return s[0], s[-1]
print(sorted(a, key=fn))
-> ['abc', 'cfc', 'cde']
'''
