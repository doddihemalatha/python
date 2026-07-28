initial_balance = 10000
withdraw_amount = int(input("Enter Withdraw Amount:"))

if withdraw_amount<=0:
    print("Invalid Amount")
elif initial_balance<withdraw_amount:
    print("Insufficient Balance")
elif withdraw_amount%100!=0:
    print("Enter Amount in multiples of 100")
else:
    print("-"*20)
    print("Withdrawal Successful")
    remaining_balance=initial_balance-withdraw_amount
    print("Remaining Balance:",remaining_balance)
