# # 함수선언(define)
# def toaster(bread):
#     print(f'{bread}이 구워지고 있다.')     ##==system.out / 내눈에 보이는것, 시스템 상에서는 아무
#     return f'구워진{bread}'               ##실제 함수 사용으로 시스템 상에서도 변경되는 값?
#
# # 함수 사용
# dish = toaster('식빵')
# print(dish)

# 반환타입:o 매개변수:o 인형뽑기
def 토스트기(bread):
    print(f'{bread}가 구워진다.') # 실질적 동작 아님, 사람 눈에만 보이는 것
    return f'구워진 {bread}' # 실제 밖으로 나오는 값

#사용
dish = 토스트기('종이') # return으로 나온 값을 dish에 담는다.
# print(dish) # dish 안의 값을 출력
print(토스트기('감자')) #토스트기에서 나온 값을 바로 출력


# 반환타입:o 매개변수:x 번호표
def 번호표기계():             ##번호표기계를 만들었어 선언
    return "번호표"          ##번호표기계가 호출(사용)되면 "번호표"라는 값을 뱉을꺼야

print(번호표기계())           ##번호표기계가 호출(사용)되면 뱉는 값을 출력해라

# 반환타입:x 매개변수:o 오락실게임
def game(coins):
    print(f'{coins}원의 게임이 시작됩니다.')
game(500)

# 반환타입:x 매개변수:x 호출벨
def bell():
    print('호출')
bell()


#zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz 내가 해본 망작
# # 반환타입:o 매개변수:o 인형뽑기
# def gacha(coin):
#     return f'인형이 나온다'
# hand = gacha({'100원'})
# print(hand)
#
# # 반환타입:o 매개변수:x 번호표
# i = 5
# def number():
#     return f'{i}번 번호표'
# finger = number()
# print(f'{i}번 번호표 나온다')
#
# 반환타입:x 매개변수:o 오락실게임
# def game(coins):
#     print(f'{coins}원의 게임이 시작됩니다.')
#
# 반환타입:x 매개변수:x 호출벨
# def bell():
#     print('호출')