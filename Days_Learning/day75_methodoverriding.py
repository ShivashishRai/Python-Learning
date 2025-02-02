
#Overrides parent class method from child class

#parent class
class Cricket():
    def __init__(self,country,format,ranking):
        self.country = country
        self.format = format
        self.ranking = ranking

    def domstic(self):
        print(f"Welcome to Domestic cricket of {self.country} ")

#derived class
class T20(Cricket):
    def __init__(self,teams):
        super().__init__("India","T20","1ST")    #inherting the parent constructor
        self.teams = teams
        super().domstic()                        #accessing the parent class method from derived class

    def domstic(self):
         print(f"League Teams {self.teams}")

#instanciating the class object
t20 = T20("RCB")
t20.domstic()





