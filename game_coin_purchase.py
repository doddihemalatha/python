#game_coin_purchase using if-else

one_coin=10
no_of_coins=int(input("Enter Number of Coins:"))
total_amount=one_coin*no_of_coins

if total_amount>=500:
    print("Bonus: 50 Extra Coins")
else:
    print("No Bonus Coins")
print("Number of Coins Purchased",no_of_coins)
print("Total Amount:",total_amount)
