age = int(input("Enter your Age:"))

if age >= 21:
    salary = int(input("Enter your salary:"))
    if salary >= 30000:
        credit_score = int(input("Enter Your Credit Score:"))
        if credit_score >= 750:
            print("Congratulations! \nLoan Approved")
        else:
            print("Loan Rejected \nLow Credit Score")
    else:
        print("loan Rejected \nSalary should be at least 30,000")
else:
     print("Not Eligible \nAge should be 21 or above")
