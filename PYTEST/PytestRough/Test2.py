import pytest

def test_divisible_by_15(input_total):
    assert input_total%15 == 0

def test_divisible_by_7(input_total):
    assert input_total%7 == 0