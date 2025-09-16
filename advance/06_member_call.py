class Car:
    # gear,on은 멤버 변수 또는 멤버 필드라고 한다.
    gear = 0
    on = False

    # 생성자 - 클래스를 사용하기 위해서 객체화를 해야 하기 때문에 생성자는 필수이다.
    # 그런데 프로그래밍의 규칙 중 하나는 너무 당연하게 있어야 할 것들은 생략이 가능하다.
    def __init__(self):
        # 혹시나 기어가 들어가 있거나 시동이 켜있을 수 있어 초기 상태로 되돌려 놓는다.
        self.gear = 0
        self.on = False

    #멤버 함수 - 클래스 안의 생성자 함수들은 해당 객체를 표시하기 위한 self를 기본으로 가지고 있는다.
    def start(self):
        if self.on == False:                ##시동이 꺼져있는 상태
            print('시동이 걸렸습니다.')        ##시동이 걸렸습니다 라고 출력
            self.on = True                  ##실제로 시동이 걸린 상태로 바꿔
        else:
            print('시동이 이미 걸려있습니다.')

    def change(self,gear):         ##여기 gear는 매개변수
        print(f'{gear} 단으로 변속 했습니다.')
        self.gear += gear          ##매개변수로 받아온 gear가 self.gear가 될 것 class gear에도 들어감???????????

# Car 클래스를 객체화(복사)
# 객체를 통해 사용하고 싶은 멤버 호출
car = Car()      ##class Car를 car라는 변수로 객체화
# 시동 걸기
car.start()
# 변속하기
car.change(3)
print(f'현재 car의 gear 단수 : {car.gear}')