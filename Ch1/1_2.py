# 特殊方法(__xx__())的存在是为了给解释器调用的，而不是直接使用
# __repr__()   repr()函数默认给机器看  如 s=’a‘  repr(s)='a'
# __str__()  str()函数默认给用户看,更加用户友好  如 s='a' print(s)=str(a)=a

from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        返回str(object) or repr(object)
        :return:
        """
        return "'Vector({}, {})'".format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# ====================test()=================== #
v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(abs(v2))
print(str(v1 + v2))
print(repr(v2))
print(v1 * 3)
print(bool(v1))
