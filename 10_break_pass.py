cup = 0
running = True

while running:
    cup += 1                #cup이라는 변수를 1씩 증가시킨다
    print(cup)
    if cup == 10:
        #running = False -> 기존에 멈추던 방식
        break

print('while 문 종료')