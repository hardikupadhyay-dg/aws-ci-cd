import pytest
from src.calculator import add, subtract, product

def test_add():
    assert add(3, 5) == 8

def test_subtract():
    assert subtract(10, 4) == 6

def test_product():
    assert product(3, 4) == 12
