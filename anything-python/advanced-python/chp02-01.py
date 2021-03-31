# 클래스 구조
## 구조 설계 후 재사용성 증가
## 코드 반복 최소
## 메소드 활용


# class Car(object):   # object class를 상속받음. 쓰지 않아도 상관은 없음.
class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details        # 파이썬에서의 언더스코어 https://mingrammer.com/underscore-in-python/

    def __str__(self):
        # 인스턴스 메서드
        # 사용자 레벨에서 print문으로 문자열로 출력하는 방식 (비공식적)
        # 구현이 된 경우, 클래스 인스턴스 내부의 속성 정보를 출력할 수 있음.
        # 기본적으로 str이 repr보다 우선순위가 높음.
        return "str : {} - {}".format(self._company, self._details)

    def __repr__(self):
        # 인스턴스 메서드
        # 개발자 레벨에서 자료형의 타입에 따른 객체를 그대로 출력하는 방식 (공식적)
        return "repr : {} - {}".format(self._company, self._details)


if __name__ == "__main__":
    car1 = Car("Ferrari", {'color': 'red', 'horsespower':'450', 'price':'8000'})
    car2 = Car("BMW", {'color': 'gray', 'horsespower': '500', 'price': '10000'})
    car3 = Car("McLaren", {'color': 'orange', 'horsespower': '400', 'price': '7000'})
    print(car1)
    print(car1.__dict__)
    print(dir(car1))


## 그외 메모
# __dict__ : car1.__dict__ 클래스의 속성을 모두 딕셔너리 형태 볼 수 있음
# dir() : dir(car1) 클래스 내 모든 메타 정보에 대한 옵션을 볼 수 있
