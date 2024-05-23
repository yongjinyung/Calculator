from calculator.calculator import Calculator
import pytest
class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_add_negative(self):
        # arrange
        a = -1
        b = -1
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = -2
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 4444
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3210
        assert result == expected

    def test_subtract_negative(self):
        # arrange
        a = -5
        b = -3
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = -2
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 4444
        b = 1
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 4444
        assert result == expected

    def test_multiply_by_zero(self):
        # arrange
        a = 4444
        b = 0
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 0
        assert result == expected

    def test_divide(self):
        # arrange
        a = 4444
        b = 1111
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 4
        assert result == expected

    def test_divide_by_zero(self):
        # arrange
        a = 4444
        b = 0
        cal = Calculator()

        # act
        with pytest.raises(ZeroDivisionError):
            cal.divide(a, b)

        # assert
        
    def test_divide_negative(self):
        # arrange
        a = -4444
        b = 1111
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = -4
        assert result == expected


