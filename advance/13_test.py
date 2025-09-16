#1.사용자가 문자를 넣으면? -> ValueError
#2.숫자를 입력하세요 출력
#3.숫자 입력할때까지 계속 돌게 하기

#첫 시도 ---------------------> 실패!!!!!!!!!
# try:
#     text = input('값을 넣으면 숫자로 변환 됩니다.')
#     num = int(text)
#     print(f'당신이 입력한 값:{num}이 숫자로 변환 되었습니다.')
# except ValueError:
#     print('***숫자를 입력해주세요.***')
#     running = True
#     while running:
#         text = input()
#         num = int(text)
#         print(f'당신이 입력한 값:{num}이 숫자로 변환 되었습니다.')
# finally:
#     print('=============끝===============')


#피드백 받고 다시 만들어봄 --------------------> 실패! ====> 결국 못풀었기 때문에 깃헙에서 다시 리뷰하기!!!!!!!!!!!!!!!!!!
#1.숫자를 넣을 때까지 계속 물어봄
#2.exception 에서 탈출
# running = True
# while running:
#     try:
#         text = str(input('값을 넣으면 숫자로 변환 됩니다.'))
#         print('***숫자를 입력해주세요.***')
#     except ValueError:
#         print('***숫자를 입력해주세요.***')
#         text = input()
#         num = int(text)
#         print(f'당신이 입력한 값:{num}이 숫자로 변환 되었습니다.')
#         if text == str():
#             running = False

#이것이 정답임.....이렇게 간단한거임..............나는 바보멍충이똥개임
while True:
    try:
        text = input('값을 넣으면 숫자로 변환 됩니다.')
        num = int(text)
        print(f'당신이 입력한 값:{num}이 숫자로 변환 되었습니다.')
        break
    except ValueError:
        print(f'{text}는 숫자가 아닙니다. 숫자를 입력하세요.')



#문자를 넣으면 문자가 나오게 하는 문제?
#1.사용자가 문자를 넣으면 -> ValueError
#2.input 변수인 text를 문자함수?에 넣고 str 변수에 담아
#3.문자가 문자로 변환 되었다. 출력 - 끝
# try:
#     text = input('값을 넣으면 숫자로 변환 됩니다.')
#     num = int(text)
#     print(f'당신이 입력한 값:{num}이 숫자로 변환 되었습니다.')
# except ValueError:
#     str = str(text)
#     print(f'당신이 입력한 값:{str}이 문자로 변환 되었습니다.')
# finally:
#     print('=============끝===============')