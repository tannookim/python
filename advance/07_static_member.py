class Robot:
    count = 0

    def how_count(self):
        print(f'객체 매서드:{self.count}')

    @classmethod # 원본영역의 변수를 건드릴 수 있다는 표시 ##이게 없으면 원본 밖에서 원본 매소드를 사용했을 때 self 없다고 오류뜸.
    def std_count(self):                       ##멤버매서드이기 때문에 무조건 self를 넣어줘야함.
        print(f'클래스 매서드:{self.count}')

r1 = Robot()      ##class Robot의 객체(복사본) r1과 r2는 전혀 다른 객체임.
r2 = Robot()
# r1 과 r2 는 서로 다른 객체이므로 count 를 건드렸을때 서로 영향받지 않는다.
r1.count += 1
print(f'r1.count:{r1.count}')
print(f'r2.count:{r2.count}')
r2.count += 100
print(f'r1.count:{r1.count}')
print(f'r2.count:{r2.count}')

# 원본의 내용을 고치고 싶다면? 원본으로 직접 가서 고쳐야 한다.
Robot.count = 1000            ##원본 데이터를 수정해도 객체(복사본)의 데이터가 수정되지 않는다. 서로 다른 영역에 있기 때문에 영향 받지 않는다.
# 원본(static)영역에서 고쳤을때 당연히 복사본(heap)영역에는 영향이 없다.
print(f'r1.count:{r1.count}')
print(f'r2.count:{r2.count}')
r1.how_count()
r2.how_count()

# 마찬가지로 원본의 내용을 확인하고 싶다면 원본영역으로 가서 확인해야 한다.
print(f'원본 count: {Robot.count}')
Robot.std_count()                  ##너 왜 셀프 없어? TypeError: Robot.std_count() missing 1 required positional argument: 'self'