##x,y 중에 뭐가 더 큰지 출력해주는 함수를 만들고 api로 만들어주는 내용
def print_max(x,y):
    '''
    입력된 x와 y 중 큰 값을 알려주는 함수 입니다.
    :param x: 인자값1
    :param y: 인자값2
    '''


    print(f'{x}와{y} 중에...')
    if x > y:
        print(f'{x}가 더 큽니다.')
    else:
        print(f'{y}가 더 큽니다.')

print_max(5,10)

# 해당 함수에 대한 출력
print(f'함수설명:{print_max.__doc__}')