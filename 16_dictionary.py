# dictionary는 {key:value} 형태로 되어 있다.  ##list=[] / tuple=() / dictionary={}
# 비슷한 자료구조로는 자바스크립트에는 오브젝트, 자바의 맵이 있다.

dic1 = {'name':'Kim,sungeun',
        'phone':'010-1234-1234',
        'age':'55'
       }

dic2 = {'name':'HGD',
        'phone':'010-9876-5432',
        'friends':['Alice','John','Smith']
       }


##사전에 데이터 넣기 두가지 방식 모두 알고 있기!
# 사전에 데이터 넣기 1 ##사전을 최초로 생성할때 쓰는 방법이라고 생각하면 됨.
a ={'first':'a'}
print(a)

# 사전에 데이터 넣기 2 ##생성되어 있는 사전에 데이터를 추가하거나 수정할 때 사용하는 방법이라고 생각하면 됨.
a['second'] = 'b'
print(a)

## a ={'first':'a'} 라는 사전을 만들었고 a['key이름']='value' 공식에 새로 추가하려는 key이름과 그 key의 값을 value 자리에 넣으면 됨.

# 사전에서 특정 요소 삭제
del a['second']
print(a)

# 사전의 특정 요소를 꺼내보자(사용법은 list와 비슷하다)
print(dic2['name'])
print(dic2['friends'])
# get 매서드(함수)를 활용해서도 가져올 수 있다.
print(dic2.get('phone'))
# 특정 키가 없는 경우 None이 아닌 대체 내용으로 반환 할 수 있음
print(dic2.get('nick','해당 내용이 없음'))
