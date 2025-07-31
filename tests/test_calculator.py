import unittest
import pytest
from hwpack_calculator import calculator

# pytestでの実行はデフォルトで「unittestのテスト」も実行
# unittest           : python -m unittest tests/test_calculator.py
# pytest + unittest  : pytest tests/test_calculator.py

# 単体
# ========== unittest Ver. ==========
class TestCalculator(unittest.TestCase):
    # Positive Test（正常系テスト）
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 5), 10)

    def test_divide(self):
        self.assertEqual(calculator.divide(20, 5), 4)

    # Nagative Test（異常系テスト）
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(5, 0)


# =========== pytest Ver. ===========
# Positive Test（正常系テスト）
def test_add_py():
    assert calculator.add(2, 3) == 5

def test_subtract_py():
    assert calculator.subtract(5, 2) == 3

def test_multiply_py():
    assert calculator.multiply(2, 5) == 10

def test_divide_py():
    assert calculator.divide(20, 5) == 4

# Negative Test（異常系テスト）
def test_divide_by_zero_py():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(5, 0)


# 結合
# ========== unittest Ver. ==========
class TestCalculatorIntegration(unittest.TestCase):
    def test_combined_calculator(self):
        add = calculator.add(2, 3)
        multiply = calculator.multiply(add, 4)
        subtract = calculator.subtract(multiply, 5)
        divide = calculator.divide(subtract, 3)

        self.assertEqual(divide, 5)


# =========== pytest Ver. ===========
def test_combined_calculator_py():
    add = calculator.add(2, 3)
    multiply = calculator.multiply(add, 4)
    subtract = calculator.subtract(multiply, 5)
    divide = calculator.divide(subtract, 3)

    assert divide == 5


if __name__ == "__main__":
    unittest.main()
