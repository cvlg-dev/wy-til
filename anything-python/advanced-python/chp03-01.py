

class Fruit:
	def __init__(self, name, price):

		self._name = name
		self._price = price

	def __str__(self):
		return "Fruit Class Info: {},  {}".format(self._name, self._price)

	def __add__(self, x):
		print("called >> __add__")
		return self._price + x._price

	def __sub__(self, x):
		print("called >> __sub__")
		return self._price - x._price

	def __le__(self, x):
		print("called >> __le__")
		if self._price <= x._price:
			return True
		else:
			return False

	def __ge__(self, x):
		print("called >> __ge__")
		if self._price >= x._price:
			return True
		else:
			return False			


s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# 매직메소드 통한 인스턴스간 연산
## 내부적으로 s2가 x로 인자가 전달 됨
print(s1 + s2)
print(s1 - s2)
print(s1 >= s2)
print(s1 <= s2)

# 매직메소드 __str__
print(s1)
print(s2)
