
#Difference b/w methods
'''
instance method                                    class method
------------------------------------------------------------------------------------
uses atleast one instance variable                no instance variables used
uses atleast one instance and static variable     only contain static variables
no decorator                                      @classmethod is required as decorator
self is passed as first argument                  cls is passed as first argument (i.e. class object)
(i.e. reference to current object)

call by object reference                          call by eiter classname or by object reference recommended to use classname.classmethod

'''

#Important to Note
    # static method can be used without @staticmethod decorator
    # if we are not using decorators it can be either static or instance method
        #based on the way of accessing
            # if we trying to access by classname.staticmethodname ::::> static_method
            # if we trying to access by objectreference.staticmethodname  :::> instance_method