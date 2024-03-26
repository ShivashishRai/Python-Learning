
#WAP to calculate the simple interest

#functon to calculate the simple interest
def si(pamt, rate, time):
    simple_interest = (pamt*rate*time)/100
    print(f"Simple Interest calculated is : {simple_interest}")

pamt = int(input("Enter the Prinicple amount: "))
rate = float(input("Enter the rate of interest : "))
time = int(input("Ente the time for the interest calculation: "))

#calling the function
si(pamt,rate,time)
