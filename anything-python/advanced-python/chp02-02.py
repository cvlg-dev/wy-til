
class Car:
    """ ## Pythonic 한 방식으로 코멘트를 달아주는 것이 좋다
    Car class
    Author  : Lucas
    Date    : 20210331

    """

    # 클래스 변수 : namespace는 없는데 접근은 가능함.
    car_count = 0



    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return "str : {} - {}".format(self._company, self._details)

    def __repr__(self):
        return "repr : {} - {}".format(self._company, self._details)

    def detail_info(self):
        print("Current ID: {}".format(id(self)))
        print("Car Detail Info: {} {}".format(self._company, self._details.get("price")))





car1 = Car("Ferrari", {'color': 'red', 'horsespower': '450', 'price': '8000'})
car2 = Car("BMW", {'color': 'gray', 'horsespower': '500', 'price': '10000'})
car3 = Car("McLaren", {'color': 'orange', 'horsespower': '400', 'price': '7000'})


# ID
print(id(car1))
print(id(car2))
print(id(car3))


# dir & __dict__
## 모든 클래스는 object를 상속받고 있고,
## dir는 해당 인스턴스가 가지고 있는 모든 어트리뷰트를 출력한다.
## __dict_는 클래스의 namespace만 딕셔너리 형태로 출력
print(dir(car1))
print(dir(car2))
print(dir(car3))
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# __doc__
## 협업을 위해 적은 document
print(car3.__doc__)


# custom method
car3.detail_info()


# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__) == id(car2.__class__) == id(car3.__class__))


# self의 의미
## 인스턴스 메소드.
## self를 통해서 인스턴스 내 attribute 정보를 관리할 수 있음

# 인스턴스 변수
## namespace를 가지고 있다.
## 인스턴스에서만 할당되는 변수
## self를 통해서만 접근 가능
print(car1._company == car2._company)
print(car1 is car2)


# 클래스 변수
## namespace는 없는데 접근은 가능함.
## 모든 인스턴스가 공통적으로 공유하는 클래스의 변수
## 하나의 클래스에서 공통적으로 참조하는 변수가 있을 때 사용
print(car1.car_count)
print(car2.car_count)
print(car3.car_count)
print(dir(car1))
print(dir(car2))
print(dir(car3))
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)



