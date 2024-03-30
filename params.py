import pytest


@pytest.fixture(params=[("Shiv",191),("Puju","MyLove")])

def myfix(request):
    return request.param



def testcallfix(myfix):
    print(myfix[0])