import pytest
'''we can group tests on basis of markers:  @pytest.mark.<markername>  '''

def test_m3():
    assert True


def test_m4():
    assert False


@pytest.mark.home
def test_m5():
    assert 100 == 100


@pytest.mark.login
def test_login_Insta():
    assert "admin24" == "admin13"


'''to run tests/files

    pytest -v (now it runs tests from both test_demo1 & test_demo2 also)
    pytest test_demo2.py -v (to run only tests from demo2)
    pytest PytestSessions/test_demo2.py -v (mentioning the path)

    #to run only tests with login substring/keyword   
    pytest -k login -v    (k -> substring) (it will run from both demo2 and demo3)

    #to run only a test of demo2 i.e, a subtest of demo2,
    pytest -k Insta -v    (k -> substring)

'''
