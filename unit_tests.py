import unittest
from figureSquare.figuresquare import FigureSquare as figSquare


class TestSquareCalc(unittest.TestCase):
    calcOne = figSquare(5)
    calcThree = figSquare(5, 12, 13)

    def test_result_one(self):
        self.assertEqual(self.calcOne.result(), 78.53981633974483)

    def test_result_three(self):
        self.assertEqual(self.calcThree.result(), 30.0)

    def test_isrightangled_one(self):
        self.assertEqual(self.calcOne.isrightangled(), False)

    def test_isrightangled_three(self):
        self.assertEqual(self.calcThree.isrightangled(), True)


if __name__ == "__main__":
  unittest.main()
