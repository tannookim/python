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


##사전에 데이터 넣기 두가지 방식 모두 알고 있기! ##list는 숫자만 들어가고, dictionary는 문자가 들어간다.(문자도 결국 숫자라서 숫자도 넣을 수 있음)
# 사전에 데이터 넣기 1
a ={'first':'a'}
print(a)

# 사전에 데이터 넣기 2
a['second'] = 'b'
print(a)

# 사전에서 특정 요소 삭제
del a['second']
print(a)