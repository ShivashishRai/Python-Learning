# #Inner Class : Class declared inside another class
#     #without existing one type of object,if there is no chance of existing another type of object, then we should go for inner classes
#     #i.e when seprate object is not required for class we can utilise the inner class concept
# class ICC:
#     def __init__(self):
#         print("I am ICC Constructor managing all cricket board")
#     class Bcci:
#         def __init__(self):
#             print("Myself Board of Cricket Counsil of India")
#         def Ranji_Trophy(self):
#             print("Ranji Trophy is one of the Prestigious Domestic Tournament of India")
#     class Bcb:
#         def __init__(self):
#             print("Myself Bangladesh Cricket Board")
#     class Acb:
#         def __init__(self):
#             print("Myself Australia Cricket Board")
#
#
# cric_icc = ICC()            # by using cric_icc we can call any outer class method
#
# cric_bcci = cric_icc.Bcci()     #inorder to creat object for inner class we have to first create object for outer class
# cric_bcci.Ranji_Trophy()        # we are using inner class object to call the inner class method defined
# cric_bcb = cric_icc.Bcb()
#
# #ICC().Bcci().Ranji_Trophy()      # this is also valid to call inner class method but not recommended
#
#
# #Important
# # Nested Inner class : class inside an already inner class fall under the Nested inner class
#
# class ICC:
#     def __init__(self):
#         print("I am ICC Constructor managing all cricket board")
#     class Bcci:
#         def __init__(self):
#             print("Myself Board of Cricket Counsil of India")
#         def Ranji_Trophy(self):
#             print("Ranji Trophy is one of the Prestigious Domestic Tournament of India")
#
#         class IPL:
#             def __init__(self):
#                 print("I am an IPL Class offered by BCCI:")
#
#             def CSK(self):
#                 print("Chennai Super Kings: ")
#
# #Option 1
# #ICC().Bcci().IPL().CSK()              ouer class.innerclass.nestedinnerclass.methodname
#
# #OPtion 2 : more conventional and recommended way to create object linked to nested class and call method
#
# cric_icc = ICC()            # by using cric_icc we can call any outer class method
# cric_bcci = cric_icc.Bcci()     #inorder to creat object for inner class we have to first create object for outer class
# crick_ipl = cric_bcci.IPL()
# crick_ipl.CSK()


# Optimised way to write above code

class ICC:
    def __init__(self):
        print("I am ICC Constructor managing all cricket board")
        self.Bcci = self.Bcci()                    #WE ARE creating object

    class Bcci:
        def __init__(self):
            print("Myself Board of Cricket Counsil of India")
            self.ipl=self.IPL()                         #creating object for class IPL and self is class BCCI object
            self.ipl.CSK()                              # we have used class IPL object inorder to call CSK method

        def Ranji_Trophy(self):
            print("Ranji Trophy is one of the Prestigious Domestic Tournament of India")

        class IPL:
            def __init__(self):
                print("I am an IPL Class offered by BCCI:")

            def CSK(self):
                print("Chennai Super Kings: ")

cric_icc = ICC()

#Lecture : 85 revisit