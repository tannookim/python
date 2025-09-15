class Puppy:

    name="" # 멤버 변수(필드)  : class 안에서 사용 가능한 변수
    goal=""

    def __init__(self,name,goal): # 생성자 : 객체화시 호출되는 함수  ##객체화 될때 딱 한번만 불러지는 애
        # 받아온 name 과 goal 은 이 생성자를 벗어날수 없다.(생성자의 쓰임이 다하면 함께 없어진다.)
        # 그래서 클래스(객체) 멤버 에다가 넣어줘야, 객체가 살아있는 동안 사용이 가능 하다.
        # 그런데  name = name 형태로는 어떤것이 객체의 멤버인지 알 수 없다.
        # 그래서 멤버인 녀석은 self 를 이용하여 표시해 준다.
        self.name=name       ##여기서 self는 현재의 객체를 의미한다????????????
        self.goal=goal

puppy = Puppy("멍멍이","집지키기")
print(f'이름:{puppy.name} / 목적:{puppy.goal}')


#zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
class Puppy:

      name=""
      goal=""    ##Puppy라는 클래스에 name,goal이라는 멤버(변수)가 있다.

      def __init__(self,name,goal): ##객체화를 할때 초기값을 설정해주기 위해서 사용하는 생성자 ##객체화 후에 나(self)는 name과 goal 변수를 가지게 됨
          self.name=name            ##생성자의 name과 goal은 생성자 밖에 있는 변수에 영향을 줄 수 없다. => class 멤버에 저장이 안됨.
                                    ##객체화(puppy=Puppy())하고 나면 생성자는 사라지기 때문에 초기값을 기억하게 하기 위해
                                    ##생성자의 name(변수)을 class name(멤버)에 대입
          self.goal=goal            ##생성자의 name과 class의 name의 이름이 같기 때문에 생성자의 name에 self를 붙여 식별할 수 있게 한다.

puppy = Puppy("멍멍이","집지키기") ##이름은 멍멍이 목적은 집지키기로 클래스Puppy를 puppy라는 변수로 객체화 ##객체화하면 init 생성자 호출(실행)됨
print(f'이름:{puppy.name} / 목적:{puppy.goal}')