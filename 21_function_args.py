# 인자값으로 아무것도 들어오지 않았을 경우 에러를 방지 하기 위해 기본값 설정이 가능
def plus(num=0):
    result = num + 5
    return result

print(plus(5)) # => 10
print(plus()) # TypeError: plus() missing 1 required positional argument: 'num' ##값 한개는 있어야 하는데 왜 안넣었니

