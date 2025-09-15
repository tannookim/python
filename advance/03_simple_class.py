# Java에서는 파일명 == 클래스명
# 파이썬에서는 꼭 그렇진 않다.
##객체화 했을때 함수를 쓴건지 클래스를 쓴건지 헷갈릴 수 있기 때문에 클래스이름은 대문자로 쓴다.

class Student: # Student 라는 클래스-학생과 관련된 함수 및 변수가 들어오겠구나 예측 가능
    pass # pass는 함수나 클래스에 아무것도 없을 때 오류방지를 위해 넣는 키워드

std1 = Student() ## Student라는 class를 객체화(복사)해서 std1이라는 변수명에 담는 것 / 객체화 한다 == 원본 class를 복사해 오는 것
std2 = Student()
std3 = Student()
# 일련번호가 서로 다르다.
# 파이썬에서도 객체화는 복사를 의미하므로 서로 다른 객체는 같지 않다.
print(std1)
print(std2)
print(std3)