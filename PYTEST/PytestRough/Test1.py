import pytest

def test_divisible_by_5(input_total): #we are using fixture method from conftest.py
    assert input_total%5 == 0

def test_divisible_by_9(input_total):
    assert input_total%9 == 0

def test_divisible_by_10(input_total):
    assert input_total%10 == 0

