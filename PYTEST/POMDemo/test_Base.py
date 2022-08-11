import pytest


'''init__driver fixture is applied on base class and this class is inherited by other login and home test class'''
@pytest.mark.usefixtures("init__driver")
class BaseTest:
    pass