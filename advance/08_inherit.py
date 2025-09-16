##상속의 개념 : 내것처럼 사용한다.
class Runner:             ##생성자는 당연히 있어야 하는거라서 생략함.
    def run(self):
        pass

    def sprint(self):
        pass


class Jumper:
    def jump(self):
        pass

    def high_jump(self):
        pass

class Person(Jumper, Runner):
    pass