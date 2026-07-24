fixed_balance = 10000

withdraw = int(input("Enter Withdraw Amount: "))

if withdraw % 100 == 0:
    if withdraw <= fixed_balance:
        print("Withdrawal Successful")
        remaining_balance = fixed_balance - withdraw
        print("Remaining Balance:", remaining_balance)
    else:
        print("Insufficient Balance")
else:
    print("Enter amount in multiples of 100")
