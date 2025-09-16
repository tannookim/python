##자식 클래스를 객체화하면 부모 클래스를 먼저 객체화하고 자식 클래스를 객체화 한다. - 생략된 생성자의 비밀

class Parent():
    def __init__(self):
        print('부모 생성자 실행!')

class Child(Parent):
    def __init__(self):
        super().__init__() # 생략된 부모 생성자
        print('자식생성자')

ch = Child()
