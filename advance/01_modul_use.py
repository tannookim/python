# from 모듈 import 함수
# 사용할 함수를 미리 불러놓고 사용하는 방법
from oper import sum       ##oper라는 모듈에 있는 sum함수를 사용하겠다.
print(f'sum() 함수 실행:{sum(5,10)}')

# import 모듈
# 일단 모듈을 불러놓고 모듈로부터 원하는 함수를 사용하는 방법
import oper       ##oper 모듈 불러올꺼야
print(f'minus() 함수 실행:{oper.minus(10,5)}')    ##oper모듈 안에 minus함수

# import 모듈 as 모듈nick
import oper as op      ##oper모듈 불러올껀데 이름을 op라고 할게
print(f'minus() 함수 실행:{op.minus(10,5)}')

# 변수도 불러올 수 있다.
print(f'field1:{op.field1} / field2:{op.field2}')