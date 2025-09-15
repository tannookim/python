cup = 0

'''조건이 무조건 참이 될 경우 영원히 실행 되므로 멈출 수 없다.
while True:
    cup = cup+1
    print(cup)
'''


while cup<10:
    cup = cup + 1 # 이게(statement:실행할 코드==문장==최소단위 명령어) 없으면 위에 선언한 cup이 0이기 때문에 무한루프 걸려서 계속 0이 출력됨.
    print(cup)
