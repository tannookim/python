class Robot:
    # 생성자 : 객체화 할대 호출되는 함수의 일종으로 객체화가 될때 가장 먼저 호출된다.
    # self
    def __init__(self):
        print('Robot이 객체화(복사) 될때 제일 먼저 호출되는 멤버')

    def doIt(self):
        print('나는 Robot의 함수 입니다.')

robot = Robot()  ##Robot이라는 클래스를 robot이라는 변수로 객체화(복사)함.
robot.doIt()