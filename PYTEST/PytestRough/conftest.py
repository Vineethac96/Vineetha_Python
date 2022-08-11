'''Create Global Pytest Fixture using Conftest.py file
By doing so, we define a fixture in conftest.py and use it within for the tests within that directory, and no need to write fixtures again and again in every test file


similar way for test_fixture_params, we create a conftest and run only tests without any fixtures in that file
Simple example'''

import pytest

@pytest.fixture
def input_total():
    total = 100
    return total

