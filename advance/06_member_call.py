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

    def change(self):
        pass

