# try 코드 안에서 여러개의 예외가 발생한 경우..
import traceback

#1. 생겨난 예외마다 각기 다른 처리를 해주고 싶은 때
try:
    pass
except IOError:
    pass
except KeyboardInterrupt:
    pass
except ValueError:
    pass
finally:

#2. 어떤 예외가 발생하던지 동일한 처리를 하고 싶을 때
try:
    pass
except Exception: # 예외(IOError,ValueError,KeyboardInterrupt 등등)의 최상위 부모이기 때문에 다른 자식 예외들이 모두 걸린다. ##단 어떤 예외가 발생했는지 상세하게 알 수 없다.
    pass


try:
    pass
except Exception as e: ##이렇게 하면 어떤 예외가 발생했는지 상세히 알 수 있다 ##일반적으로 가장 많이 사용
    traceback.print_exc()
