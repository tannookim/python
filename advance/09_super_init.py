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
