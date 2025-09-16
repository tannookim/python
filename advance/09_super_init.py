##자식 클래스를 객체화하면 부모 클래스를 먼저 객체화하고 자식 클래스를 객체화 한다. - 생략된 생성자의 비밀

class Parent():
    def __init__(self):
        print('부모 생성자 실행!')

class Child(Parent):
    def __init__(self):
        super().__init__() # 생략된 부모 생성자  ##super은 부모 클래스를 지칭
        print('자식 생성자 실행!')

ch = Child()

# 부모가 초기화가 필요하다면 자식에게 값을 전달해서 자식이 부모에게 전달하도록 한다.
class SchoolMember:  # 부모

    name = ''
    age = 0

    def __init__(self, name, age): # 3. 받아온 값으로 초기화 하고 객체화 된다.
        self.name = name
        self.age = age

class Teacher(SchoolMember):  # 자식
    salary = 0

    def __init__(self, name, age, salary):    ##salary는 내가 쓸꺼고 name,age는 부모 클래스로 전달해야됨.
        super().__init__(name, age)           # 2. 부모를 먼저 객체화 시키면서 초기화 할 값을 전달  ##부모클래스에 name, age 넣어야하니까 super()
        self.salary = salary                  # 4. 그리고 나서 내(자식)가 초기화 하면서 객체화 된다.

# 1.Teacher 라는 클래스를 객체화 한다.(초기화를 위해 인자값(매개변수)를 전달)
t = Teacher('김철수',33,5000000)
# 5.name 과 age 는 부모 것 이지만 내(자식)것처럼 내(자식) 객체에서 가져다 쓸 수 있게 된다.
print(f'{t.name}({t.age})-{t.salary}')


#생성자 전달 순서 설명 - 나의 언어로
class SchoolMember:                        ##부모 클래스
    name = ''
    age = 0

    def __init__(self, name, age):         ##4-전달받은 값으로 초기화하고 객체화한다.
        self.name = name                   ##=>부모 객체의 name(self.name)에 받아온 name을 넣는다 라는 뜻
        self.age = age

class Teacher(SchoolMember):               ##SchoolMember(부모)를 상속 받은 자식 클래스
    salary = 0

    def __init__(self, name, age, salary): ##2-자식클래스(Teacher)를 객체화하면 부모클래스(SchoolMember)가 먼저 객체화한다.
        super().__init__(name, age)        ##3-부모 클래스의 필드값(name,age)을 super()함수를 이용해 부모의 생성자로 전달한다.
        self.salary = salary               ##5-부모가 객체화되고 자식이 나의 필드값(salary)으로 초기화 하고 객체화한다.

t = Teacher('김철수',33,5000)  ##1-자식 클래스 Teacher를 각 인자값(김철수,33,5000)으로 초기화(초기값을 넣는다)하고 t라는 변수로 객체화한다.
print(f'{t.name}({t.age})-{t.salary}')  ##6-객체화 할때 부모가 먼저 객체화 되었기 때문에 부모의 멤버도 내것처럼 쓸 수 있다. 부모를 상속 받은 자식의 객체에서 부모의 필드도 사용할 수 있다.