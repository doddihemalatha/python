#withdraw money

balance=float(input("Enter a balance:"))
withdraw=int(input("Enter Withdraw Money:"))

if balance>=withdraw:
    balance=balance-withdraw
print(balance)
