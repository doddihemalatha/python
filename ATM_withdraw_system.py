#ATM Withdrawal System

fixed_balance=10000
withdraw=int(input("Enter Withdraw amount:"))

if withdraw<=fixed_balance:
    print("Withdraw successfully")
    remaining_balance=fixed_balance-withdraw
    print(remaining_balance)
else:
    print("Insufficient Balance")
