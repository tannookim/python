import random #random.randint 자동완성(tab)하니까 자동 생성됨.

number = random.randint(1,31) #a,b는 자동생성임. 타이핑X #정수 1~31까지 숫자 중에 랜덤으로 하나 고를껀데 그게 number(변수명)의 값이야 정의
print(f' 내 마음속 숫자: {number}')  #내마음속숫자(텍스트)랑 {number}(숫자)가 같이 출력되어야 해서 f-string 작성해야함.
running = True #running이라는 변수가 뭔지 모르겠고 무조건 참이야 정의
while running: # running=true로 해놓고 while running 이라고 조건문을 썼으니까 명령문에서 running=false가 나올때까지 무한루프로 돌 것임.
                # while함수는 조건값이 true 일 때 계속 반복되는 구문이다. 조건값이 false가 되면 멈춤.

    guess = int(input('1~31 중 내가 생각한 숫자는?')) # 입력받은 값을 정수(int)로 변환하여 guess에 대입
                                                   # => 초록색 텍스트에 사용자가 숫자(정수(int)로)를 넣(input)을거야 그게 guess(변수명)의 값이야 정의
                                                   # int자리에 float도 올 수 있음. 그럼 실수(ex 6.3 이런 값)까지 사용자가 input 할 수 있음.
    print(f'입력받은 숫자 : {guess}')
    if guess == number:
        running = False #running이 true값일 때 계속 while문이 돌아가는거니까 원하는 값이 나왔을때 running=false로 대입해야 정답을 맞췄을 때 while문이 멈춤.
        print('정답!')
    elif guess > number:
        print('내 마음 속 숫자 보다 커요.')
    elif guess < number:
        print('내 마음 속 숫자 보다 작아요.')

   # 이런 식으로 작성할 수 있음.
    '''
    if guess > number:
        print('내 마음 속 숫자 보다 커요.')
    elif guess < number:
        print('내 마음 속 숫자 보다 작아요.')
    else guess == number:
        print('정답!')
        running = False
    '''