#파스칼표기법 - 맨 앞글자만 대문자(Java의 Class 생성 시 활용)
#카멜표기법 - 단어의 의미가 있는 첫글자를 대문자로 한다.(shopList) / 대중적으로 많이 쓰는 표기법
#스네이크표기법 - 단어간의 구분을 _로 한다.(shop_list) / 파이썬에서 주로 사용



# 리스트 생성 방법1 - 비어있는 리스트로 생성. 아무 값이나 데이터 없이 리스트만 만드는 것.
a = []             #[]는 맥주 샘플러 판떼기 같은 개념임.

# 리스트 생성 방법2 - 값이 있는 리스트로 생성
shop_list = ['apple','mango','carrot','banana']
print(f'shop_list:{shop_list}')

# 리스트에 값을 넣는 방법
# 가장 뒤로 넣는 방법
a.append(1)         #얘 지금 0번방에 있음
a.append(2)         #얘 지금 1번방에 있음
a.append(3)
# 특정한 번호를 지정해서 넣는 방법
a.insert(1,'x')   #index 자리가 방번호임. object 는 넣으려는 값(데이터).

print(f'a의 길이 : {len(a)}')
print(f'a:{a}')
# a의 2번방에 있는 값 출력
print(f'a[2]={a[2]}')
# a의 가장 마지막 방에 있는 값 출력
print(f'a의 마지막 방의 값={a[3]}')    #내가 마지막 방의 값이 '3'이라는 것을 알고 숫자 3을 넣은 경우

# 길이에서 1을 뺀 값을 이용 - 인덱스는 0번부터 시작한다는 점을 이용 #리스트 길이를 구해서 마지막 방의 값을 구한 경우
print(f'a의 마지막 방의 값={a[len(a)-1]}')

# 파이썬에서 사용되는 방식, 0보다 뒤로가면 맨 뒤로 이동된다는 개념 #파이썬에서만 제공하는 개념! 0번째 방에서 -1하면 마지막 방으로 간다고 인정해줌.
print(f'a의 마지막 방의 값={a[-1]}')


# 리스트 정렬(sort)
shop_list.sort() # 오름차순 정렬
print(f'shop_list:{shop_list}')

shop_list.sort(reverse=True) # 내림차순 정렬
print(f'shop_list:{shop_list}')

# sorted 는 원본의 리스트를 정렬한 값을 새로운 리스트로 반환. 원본은 훼손하지 않고 새로운 리스트를 만든다.
new_list = sorted(shop_list)
print(f'new_list:{new_list}')

# a의 2번 index(방)에 c를 넣는다.
# insert 와 다른점은 해당 인덱스의 값을 지우고 그 자리에 들어간다는 것이다.
a[2] = 'c'       #리스트 a의 2번 인덱스의 값을 c로 변경한다.
print(f'a:{a}')

# list 삭제
del a[1]         #리스트 a의 1번 인덱스의 값을 지운다.
print(f'a:{a}')
