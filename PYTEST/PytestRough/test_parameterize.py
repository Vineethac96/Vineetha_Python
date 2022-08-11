import pytest

'''making test run for diff set of data'''
@pytest.mark.parametrize('num','res',[(2,22),(3,33)(5,55)(6,36)])
def calc(num,res):
    assert 11*num == res