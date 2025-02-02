
def calgmean(num1,num2):   #function to caluclate the geomatric mean
    mean= (num1*num2)/(num1+num2)

    print(mean)


calgmean(18,19)        #calling the function with passing argument at run time
calgmean(88,111)

num1=int(input("Enter one more number :"))      #taking run time input to be pass as argumnet to call function
num2=int(input("Enter one more number :"))
calgmean(num1,num2)


def passexample():
    pass              #just an example to pass the function