import pytest

#defining the fixture with passing parameters
@pytest.fixture(params=[("Shiv",191),("Puju","MyLove")])
def myfix(request):
    return request.param              #request is the instance object for the fixture use whenever we pass param

#invocing the fixture 
def testcallfix(myfix):
    
    print(myfix[0])
