case_no = int(input("Enter the value of the case to be matched: "))

match case_no:
    case 10:
        print("Entered case is 10")

    case 20:
        print("Entered case if 20")

    #default value to be executated if above cases are not matching
    case _ if case_no % 13==0:
        print("Case no is divisible by 13")


