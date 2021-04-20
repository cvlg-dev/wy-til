# 매직매소드를 통한 벡터 연산 예제



class Vector:

    def __init__(self, *args):
        """
        Create a vector, example:  v = Vector(5, 10)
        """

        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args


    def __repr__(self):
        """
        Return vector informations.
        """
        return "Vector(%r, %r)" % (self._x, self._y)


    def __add__(self, other):
        """
        Return vector addition of self and other
        """
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)


    def __bool__(self):
        return bool(max(self._x, self._y))


v1 = Vector(5, 8)
v2 = Vector(25, 20)
v3 = Vector()


print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print(v1, v2, v3)

# 연산
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2))
print(bool(v3))
