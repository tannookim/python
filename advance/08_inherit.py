##상속의 개념 : 내것처럼 사용한다.
class Runner:             ##생성자는 당연히 있어야 하는거라서 생략함.
    def run(self):
        print('달린다.')

    def sprint(self):
        print('전력질주를 한다.')


class Jumper:
    def jump(self):
        print('점프를 한다.')

    def high_jump(self):
        print('높이 점프를 한다.')


class Person(Jumper, Runner): # Jumper 와 Runner 를 상속 받았다.
    def walk(self):
        print('걷는다.')

# walk() 함수를 사용하기 위해 Person 클래스를 객체화한다.
p= Person()
p.walk()

# 상속 받은 함수(매소드)들을 내것처럼(p객체로부터) 사용한다.
p.jump()
p.high_jump()
p.run()
p.sprint()