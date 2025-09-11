cup = 0
running = True

# while running:
#     cup += 1                #cup이라는 변수를 1씩 증가시킨다
#     print(cup)
#     if cup == 10:           #cup 이 10이 되면
#         #running = False    -> 조건을 거짓으로 대입해 멈추는 방식
#         break
#
# print('while 문 종료')

for i in range(1,10):         # 변수 i의 범위는 1~9까지
    if i ==3:                 # 변수 i의 값이 3이라면
        continue              # 위 조건 무시하고 지나가
    if i ==6:                 # 변수 i의 값이 6이라면
        continue
    if i ==9:                 # 변수 i의 값이 9이라면
        continue
    print(i)



for i in range(1,10):
    if i ==3 | i ==6 | i ==9 :
        continue
    print(i)

for i in range(1,10):
    if i %3 == 0:
        continue
    print(i)