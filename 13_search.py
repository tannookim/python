# 검색 -> 특정한 자료 덩어리에서 원하는 값을 찾는 것
a = [3,4,1,2,3,4,'G','F','G']
# 원하는 값의 인덱스 찾기
# 2라는 값은 어느 위치에 있는가?
print(f'2는 어디?:{a.index(2)}')   ##리스트 a에서 숫자2는 몇번 인덱스(몇번째 자리)인지 출력
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

#idx = 0
#while True:
#    idx = b.index(3,idx)      ##리스트 b에서 변수 idx 값부터 숫자 3을 idx번 인덱스부터 찾아라
#    print(f'3의 값은 {idx}번에 있다.')  ##몇번 인덱스에 있는지 출력
#    idx += 1  ##찾은 인덱스 번호에 1을 더하고 idx = b.index(3,idx) 반복 => 마지막 3의 인덱스 번호까지 찾고나면 더이상 3이 없다는 에러 메세지가 뜸.

idx = 0
for n in b:  # for in 을 이용하면 list에 있는 값을 순서대로 하나씩 뽑아낸다.
    if n == 3:
        print(f'3이 있는 인덱스 : {idx}')
    idx += 1

# 리스트 요소 삭제
# del a[3]과 a.remove(3) 의 차이
# del은 특정 인덱스의 값을 지운다.
# remove는 해당 값을 지운다.(처음 찾은 것만 지운다)
print(f'a:{a}')
a.remove(3)
print(f'a:{a}')

# pop() = append()의 반대개념
# 맨마지막 요소를 빼낸다.(리스트에서는 사라진다.)
val = a.pop()
print(f'빼낸 값 : {val} / a: {a}')
val = a.pop()
print(f'빼낸 값 : {val} / a: {a}')

# 리스트 확장(더하기와 비슷한 개념)
print(a)
a.extend(b)    ##리스트에 a에 b를 더(확장)한다.
print(a)

# count(val) 특정한 값이 해당 리스트에 몇개 있는지 확인해주는 것
print(a)
print(f'a안에 3인 값은 {a.count(3)}개 있다.')  ##리스트 a에 '3' 몇개 있는지 출력
print(f'a안에 9인 값은 {a.count(9)}개 있다.')  # 없는 값은 0을 반환

# a 안에 있는 모든 3을 지워주세요.
#print(a)
#idx = 0
#for n in a:
    #if n == 3:
        #del a[idx]
    #idx += a.index(n)
    #print(a)                    ##여기까지 내가 해본거 => 실패작!


# 이렇게 할 수 있다.
# for n in a:            ##리스트 a에서 값을 하나씩 뽑아서 n이라는 변수에 대입할거야
#     if n == 3:         ##n값이 3과 같다면
#         a.remove(3)    ##리스트 a에서 '3' 삭제
# print(a)

while True:
    a.remove(3)          ##리스트 a에서 '3' 삭제
    if a.count(3) == 0:  ##리스트 a에서 '3'의 개수가 0과 같다면
        break            ##멈춰
print(a)















# 코드 리뷰 과제
# 리스트 b에서 3의 인덱스 번호를 모두 출력하세요.
b = [3,4,1,2,3,4,5,6,1,3,2]
idx = 0  ##0부터 시작하기 위해 idx라는 변수를 0이라고 정의
while True: ##조건이 false가 될 때까지 무한 반복하는 반복문 사용 / 숫자3의 인덱스 번호를 모두 찾을 때까지 무한 반복하기 위해.
    idx = b.index(3,idx)      ##sth.index함수는 리스트 b에서 변수 idx값(start)부터 '3'(value)의 인덱스 번호(몇번째에 있다)를 찾는 함수. 찾은 인덱스 번호(값)가 while True 아래 변수idx에 대입 됨.
    print(f'3의 값은 {idx}번에 있다.')  ##{idx}자리에 위에서 찾은 변수idx값 출력
    idx += 1  ##찾은 idx값에 1을 더함 => while문 반복
              ##1을 더하는 이유는 1을 더하지 않으면 찾은 인덱스 번호에서부터 계속 찾기 때문에 무한반복함.
              ##마지막 3의 인덱스 번호까지 찾고나면 더이상 3이 없다는 에러 메세지가 뜸. ValueError: 3 is not in list
              ##마지막 3을 다 찾고 난 후에 while 문의 조건을 false로 바꿔주는 함수가 없어서 에러 메세지가 뜬다. if .count()만큼 다 찾으면 break 이런거 넣어주면 깔끔...??????


