

class Car:
    """ ## Pythonic 한 방식으로 코멘트를 달아주는 것이 좋다
    Car class
    Author      : Lucas
    Date        : 20210331
    Description : Class, Instance, Static Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0


    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return "str : {} - {}".format(self._company, self._details)

    def __repr__(self):
        return "repr : {} - {}".format(self._company, self._details)


    # Instance Method
    # Self: 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print("Current ID: {}".format(id(self)))
        print("Car Detail Info: {} {}".format(self._company, self._details.get("price")))


    # Instance Method
    def get_price(self):
        return "Prev Car Price -> company: {}, price: {}".format(self._company, self._details.get("price"))

    # Instance Method
    def get_price_calculated(self):
        return "After Car Price -> company: {}, price: {}".format(self._company, self._details.get("price") * Car.price_per_raise)

    # Class Method
    @classmethod # 데코레이터 추가
    def raise_price(cls, per):  # classmethod는 cls 인자를 받음. 클래스변수를 접근하기 위해서는 cls를 통해서 접근
        if per <= 1:
            raise ValueError("Enter 1 or higher value")

        cls.price_per_raise = per
        return "Price increased"


    # Static Method
    @staticmethod # 데코레이터 추가
    def is_bmw(inst): # cls, self 같은 인자를 전달받지 않음
        if inst._company == "BMW":
            return "True"
        return "False"










car1 = Car("Ferrari", {'color': 'red', 'horsespower': 450, 'price': 8000})
car2 = Car("BMW", {'color': 'gray', 'horsespower': 500, 'price': 10000})
car3 = Car("McLaren", {'color': 'orange', 'horsespower': 400, 'price': 7000})

print(car1.detail_info())
print(car2.detail_info())

# 가격 정보(직접 접근)
print(car1._details.get('price'))
print(car1._details['price'])

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# # 가격 인상(클래스 메소드 미사용)
# Car.price_per_raise = 1.4

# 가격 인상(클래스 메소드 사용)
Car.raise_price(1.8)

# 가격정보(인상 후)
print(car1.get_price_calculated())
print(car2.get_price_calculated())

# Static method 인스턴스로 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
# Static method 클래스로 호출
print(Car.is_bmw(car3)) # 클래스로 호출할 수 있음. 어떠한 인스턴스에 국한받지 않기에, 이러한 사용도 가능함.