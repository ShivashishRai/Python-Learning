
def pair_sum_array(myarr, target_sum_passed):
    myarr.sort()
    first = 0
    last = len(myarr)-1

    while first <= last:
        if(myarr[first] + myarr[last]>target_sum_passed):
            last -= 1
        elif(myarr[first] + myarr[last]<target_sum_passed):
            first += 1
        elif(myarr[first] + myarr[last]==target_sum_passed):
            print("The pair with target sum is:", myarr[first] ,"&", myarr[last])
            last -= 1
            first +=1



myarr = list(input("Enter the list of element into an list: "))
target_sum = input("Enter the target sum to be searched in list:")

pair_sum_array(myarr,target_sum)