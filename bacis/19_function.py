# 함수선언(define)
def toaster(bread):
    print(f'{bread}이 구워지고 있다.')     ##==system.out / 내눈에 보이는것, 시스템 상에서는 아무
    return f'구워진{bread}'               ##실제 함수 사용으로 시스템 상에서도 변경되는 값?

# 함수 사용
dish = toaster('식빵')
print(dish)