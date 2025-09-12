tu1 = (1,2,3) # tuple은 []가 아닌 ()로 선언 / ##함수를 이용한 데이터 수정(추가) 및 삭제 불가??????
tu2 = ('a','b','c')
tu3 = (1,2,('a','b')) ##다차원도 가능

# 불러오기
print(tu1[1])
# slicing
print(tu2[1:]) ##리스트 tu2에서 1번 인덱스부터 보여주고 버릴 영역은 없음.
#더하기
print(tu1+tu2)
#곱하기
print(tu1*3)

# tuple <-> list 간의 전환 ##tuple은 수정할 수 없으니까 수정하고 싶거나 삭제하고 싶을 때 list로 변환할 수 있다.
tu2list = list(tu2)  ##tuple을 list로 변환하는 함수 list
print(f'{tu2}->{tu2list}')

list2tu = tuple(tu2list)  ##list를 tuple로 변환하는 함수 tuple
print(f'{tu2list}->{list2tu}')
