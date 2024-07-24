import pytest

class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Returns the sum of two numbers."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Returns the difference of two numbers."""
        return a - b

def test_add():
    """Tests the add method of the Calculator class."""
    assert Calculator.add(1, 2) == 3
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(0, 0) == 0

def test_subtract():
    """Tests the subtract method of the Calculator class."""
    assert Calculator.subtract(2, 1) == 1
    assert Calculator.subtract(1, 1) == 0
    assert Calculator.subtract(0, 1) == -1

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add_parametrized(a: float, b: float, expected: float):
    """Tests the add method of the Calculator class with parameterized inputs."""
    assert Calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 1, 1),
    (1, 1, 0),
    (0, 1, -1),
])
def test_subtract_parametrized(a: float, b: float, expected: float):
    """Tests the subtract method of the Calculator class with parameterized inputs."""
    assert Calculator.subtract(a, b) == expected