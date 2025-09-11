# 검색 -> 특정한 자료 덩어리에서 원하는 값을 찾는 것
a = [3,4,1,2,3,4,'G','F','G']
# 원하는 값의 인덱스 찾기
# 2라는 값은 어느 위치에 있는가?
print(f'2는 어디?:{a.index(2)}')   ##리스트 a에서 숫자2는 몇번 인덱스인지 출력
print(f'G는 어디?:{a.index('G')}') # G는 2개인데 처음 찾은 값만 알려준다.
print(f'G는 어디?:{a.index('G',5)}') # 5번 인덱스부터 'G'를 찾아라  ##리스트 a에서 5번 인덱스부터 'G'가 몇번 인덱스에 있는지 출력

# 값이 없으면 에러(예외)를 발생시킨다. => ValueError: 'H' is not in list
#print(a.index('H'))

b = [3,4,1,2,3,4,5,6,1,3,2] # 모든 3을 찾아 보세요.
print(f'3은 어디에?:{b.index(3)}')
print(f'3은 어디에?:{b.index(3)},{b.index(3,4)},{b.index(3,9)}번 인덱스')

                                ##if b==3:    ##리스트 b는 배열이라서 b==3 이라고 물어볼 수가 없음

# idx = b.index(3,0)
# print(f'3의 값은 {idx}번에 있다.')
# idx = b.index(3,1)
# print(f'3의 값은 {idx}번에 있다.')
# idx = b.index(3,5)
# print(f'3의 값은 {idx}번에 있다.')
# idx = b.index(3,10)
# print(f'3의 값은 {idx}번에 있다.')

idx = 0
# while True:
#     idx = b.index(3,idx)      ##리스트 b에서 변수 idx 값부터 숫자 3을
#     print(f'3의 값은 {idx}번에 있다.')
#     idx += 1

for n in b:  # for in 을 이용하면 list에 있는 값을 순서대로 하나씩 뽑아낸다.
    if n == 3:
        print(f'3이 있는 인덱스 : {idx}')
    idx += 1