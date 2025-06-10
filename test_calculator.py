import pytest
from calculator import Calculator


@pytest.fixture(scope="module")
def calculator():
    return Calculator()


@pytest.mark.parametrize(
    "number1, number2, expected",
    [
        (3, 2, 5),
        (-1, 1, 0),
        (0, 0, 0)
    ]
)
def test_add(calculator, number1, number2, expected):
    assert calculator.add(number1, number2) == expected


@pytest.mark.parametrize(
    "number1, number2, expected",
    [
        (3, 2, 1),
        (-1, 1, -2),
        (0, 0, 0)
    ]
)
def test_subtract(calculator, number1, number2, expected):
    assert calculator.subtract(number1, number2) == expected


@pytest.mark.parametrize(
    "number1, number2, expected",
    [
        (3, 2, 6),
        (-1, 1, -1),
        (0, 5, 0)
    ]
)
def test_multiply(calculator, number1, number2, expected):
    assert calculator.multiply(number1, number2) == expected


@pytest.mark.parametrize(
    "number1, number2, expected",
    [
        (6, 2, 3),
        (-6, 2, -3),
        (1, 1000000, 1e-06)
    ]
)
def test_divide(calculator, number1, number2, expected):
    assert calculator.divide(number1, number2) == expected


def test_divide_zero(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(5, 0)