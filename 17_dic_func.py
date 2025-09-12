dic = {
    'name':'hong',
    'phone':'55555555',
    'friends':['Alice','Smith','John']
}

# dic.keys() : 특정한 사전의 키들만 가져와 dict_keys라는 객체를 반환한다.
print(dic.keys())

for item in dic.keys():
    print(item)

# dict_keys -> list로 변환  ##dict_keys를 list로 변경해서 keys 라는 변수에 담는 소스
keys = list(dic.keys())
print(keys)

# dic.values() : 특정 사전의 값만 가져와 dict_values 라는 객체를 반환
print(dic.values())

# list로 변경해서 values 라는 변수에 담아보자
values = list(dic.values())
print(values)