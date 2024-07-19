import math


class FigureSquare:
    _triangle_flag = False
    _c = -100
    _b = -100
    _a = -100
    _result = -100

    def __init__(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            if (isinstance(a, (int, float)) and isinstance(b, (int, float))
                    and isinstance(c, (int, float))):
                if a + b > c and a + c > b and b + c > a:
                    self._triangle_flag = True
                    self._a = a
                    self._b = b
                    self._c = c
                    p = (self._a + self._b + self._c) / 2
                    self._result = math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
                else:
                    raise Exception("It is not the triangle sides (The sum of two "
                                    "sides of triangle must be more than the third side)")
            else:
                raise TypeError("Values must be digit")
        elif a is not None and b is None and c is None:
            if isinstance(a, (int, float)):
                if a > 0:
                    self._a = a
                    self._result = math.pi * self._a ** 2
                else:
                    raise ValueError("Value must be positive")
            else:
                raise TypeError("Value must be digit")
        else:
            raise ValueError("Count of values temporarily unsupported (count of values must be 1 or 3)")

    # Constructor for a circle square
    def isrightangled(self):
        if self._triangle_flag:
            if (self._c ** 2 == self._a ** 2 + self._b ** 2 or self._b ** 2 == self._c ** 2 + self._a ** 2
                    or self._a ** 2 == self._c ** 2 + self._b ** 2):
                return True
            else:
                return False
        else:
            print("Figure is not triangle")
            return False

    def result(self):
        return self._result
