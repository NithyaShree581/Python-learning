import pytest
from calculator import add, sub, mult, div


def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(4, 3) == 1

def test_mul():
    assert mult(2, 5) == 10

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        div(2, 0)

def test_normal_div():
    assert div(3, 3) == 1