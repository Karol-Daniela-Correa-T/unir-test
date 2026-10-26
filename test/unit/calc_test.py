import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator, InvalidPermissions


def mocked_validation(*args, **kwargs):
    return True


def mocked_denied_validation(*args, **kwargs):
    return False


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
        self.assertAlmostEqual(3.5, self.calc.add(1.5, 2), delta=0.0000001)

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())
        self.assertRaises(TypeError, self.calc.add, True, 2)

    
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(4, self.calc.substract(2, -2))
        self.assertEqual(-4, self.calc.substract(-2, 2))
        self.assertEqual(1, self.calc.substract(1, 0))
        self.assertAlmostEqual(0.5, self.calc.substract(2.5, 2), delta=0.0000001)

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())

    
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        self.assertAlmostEqual(3.0, self.calc.multiply(1.5, 2), delta=0.0000001)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_fails_with_nan_parameter(self, _validate_permissions):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())

    @patch('app.util.validate_permissions', side_effect=mocked_denied_validation, create=True)
    def test_multiply_method_fails_without_permissions(self, _validate_permissions):
        self.assertRaises(InvalidPermissions, self.calc.multiply, 2, 2)

    
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertEqual(-2, self.calc.divide(4, -2))
        self.assertEqual(0, self.calc.divide(0, 5))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

   
    def test_power_method_returns_correct_result(self):
        self.assertEqual(8, self.calc.power(2, 3))
        self.assertEqual(1, self.calc.power(5, 0))
        self.assertEqual(0.5, self.calc.power(2, -1))
        self.assertEqual(4, self.calc.power(-2, 2))
        self.assertAlmostEqual(3.0, self.calc.power(9, 0.5), delta=0.0000001)

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)

    def test_power_method_fails_with_invalid_values(self):
        self.assertRaises(TypeError, self.calc.power, 0, -1)
        self.assertRaises(TypeError, self.calc.power, -8, 0.5)

    
    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.sqrt(16))
        self.assertEqual(0, self.calc.sqrt(0))
        self.assertAlmostEqual(1.4142135, self.calc.sqrt(2), delta=0.0000001)
        self.assertAlmostEqual(1.5, self.calc.sqrt(2.25), delta=0.0000001)

    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, "16")
        self.assertRaises(TypeError, self.calc.sqrt, None)
        self.assertRaises(TypeError, self.calc.sqrt, object())

    def test_sqrt_method_fails_with_negative_number(self):
        self.assertRaises(TypeError, self.calc.sqrt, -1)
        self.assertRaises(TypeError, self.calc.sqrt, -0.5)

    
    def test_log10_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.log10(100))
        self.assertEqual(0, self.calc.log10(1))
        self.assertEqual(-1, self.calc.log10(0.1))
        self.assertAlmostEqual(0.30103, self.calc.log10(2), delta=0.00001)

    def test_log10_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log10, "100")
        self.assertRaises(TypeError, self.calc.log10, None)
        self.assertRaises(TypeError, self.calc.log10, object())

    def test_log10_method_fails_with_non_positive_number(self):
        self.assertRaises(TypeError, self.calc.log10, 0)
        self.assertRaises(TypeError, self.calc.log10, -10)

    
    def test_check_type_static_method_accepts_numbers(self):
        self.assertIsNone(Calculator.check_type(5))
        self.assertIsNone(Calculator.check_type(-3.2))
        self.assertIsNone(Calculator.check_type(0))

    def test_check_type_static_method_rejects_invalid_values(self):
        self.assertRaises(TypeError, Calculator.check_type, "5")
        self.assertRaises(TypeError, Calculator.check_type, None)
        self.assertRaises(TypeError, Calculator.check_type, True)
        self.assertRaises(TypeError, Calculator.check_type, [1])

    def test_check_types_method(self):
        self.assertIsNone(self.calc.check_types(1, 2.5))
        self.assertRaises(TypeError, self.calc.check_types, 1, "2")
        self.assertRaises(TypeError, self.calc.check_types, "1", 2)


if __name__ == "__main__":  
    unittest.main()