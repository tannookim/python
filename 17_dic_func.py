dic = {
    'name':'hong',
    'phone':'55555555',
    'friends':['Alice','Smith','John']
}

# dic.keys() : 특정한 사전의 키들만 가져와 dict_keys라는 객체를 반환하는 함수
print(dic.keys())

for item in dic.keys():
    print(item)

# dict_keys -> list로 변환  ##dict_keys를 list로 변경해서 keys 라는 변수에 담는 소스
keys = list(dic.keys())
print(keys)

# dic.values() : 특정 사전의 값만 가져와 dict_values 라는 객체를 반환하는 함수
print(dic.values())

# list로 변경해서 values 라는 변수에 담아보자
values = list(dic.values())
print(values)

# dic.items() : 사전의 키:값을 한 쌍으로 가져와 dict_items로 반환하는 함수
# 각 키와 값은 ()로 싸여 있음을 보아 tuple 이다.
print(dic.items())
# 리스트로 변환해 보면 list 안에 각 키와 값이 tuple로 저장되어 있음을 알 수 있다.
li = list(dic.items())
print(li)

# 값을 가져오기
print(dic.get('name'))  ##dic이라는 사전에서 name(키)의 값을 가져오는 함수 dic.get()
print(dic['phone'])     ##dic이라는 사전에서 phone(키)의 값을 가져오는 함수 dic[]

print('연습')
# dic 안에 있는 모든 키와 값을 키:값 형태로 출력해 보자
# 1. 키를 뽑아낸 다음, 키를 가지고 값을 뽑아내는 방식
for key in dic.keys():
    print(f'{key}:{dic[key]}')

# 2. 키와 값을 동시에 뽑아낸 다음 거기서 키와 값을 각각 추출하는 방식
for item in dic.items():
    print(f'{item[0]}:{item[1]}')



## 여기 아래는 내가 해본거.........
# tpxm = list(dic.items())
# print(f'{tpxm[0][0]}:{tpxm[0][1]}')
# print(f'{tpxm[1][0]}:{tpxm[1][1]}')
# print(f'{tpxm[2][0]}:{tpxm[2][1]}')

# print(f'{keys[0]}:{values[0]}')
# print(f'{keys[1]}:{values[1]}')
# print(f'{keys[2]}:{values[2]}')