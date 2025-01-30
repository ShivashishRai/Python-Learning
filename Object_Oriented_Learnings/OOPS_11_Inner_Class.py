#Inner Class : Class declared inside another class
    #without existing one type of object,if there is no chance of existing another type of object, then we should go for inner classes
    #i.e when seprate object is not required for class we can utilise the inner class concept
class ICC:
    def __init__(self):
        print("I am ICC Constructor managing all cricket board")
    class Bcci:
        def __init__(self):
            print("Myself Board of Cricket Counsil of India")
    class Bcb:
        def __init__(self):
            print("MyselfBangladesh Cricket Board")
    class Acb:
        def __init__(self):
            print("Myself Australia Cricket Board")


cric_icc = ICC()

cric_bcci = cric_icc.Bcci()     #inorder to creat object for inner class we have to first create object for outer class

