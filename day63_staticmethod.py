
#static method not receives the implicit first argument
#static method cannnot modify the class state

class Tourism:

    def __init__(self, country, state):
        self.country = country
        self.state = state

    @staticmethod
    def visafree(name,state):
        print("Country Name is: ", name)
        print("Capital of country is : ",state)

tourism = Tourism('India','NewDelhi')
print(tourism.visafree('Malaysia','Kualalampur'))