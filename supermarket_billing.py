# -------------------------------
# Supermarket Billing System
# -------------------------------

# Price of each item
rice_per_kg = 60
sugar_per_kg = 45
milk_per_packet = 30

# Get quantity from the user
no_of_rice = int(input("Enter How many kg of Rice: "))
no_of_sugar = int(input("Enter How many kg of Sugar: "))
no_of_milk = int(input("Enter How many Milk Packets: "))

# Calculate the cost of each item
rice_cost = rice_per_kg * no_of_rice
sugar_cost = sugar_per_kg * no_of_sugar
milk_cost = milk_per_packet * no_of_milk

# Calculate the total bill before delivery charges
grand_total = rice_cost + sugar_cost + milk_cost

# Check whether the customer gets free home delivery
if grand_total >= 1000:
    print("\nCongratulations!")
    print("You got FREE Home Delivery")
else:
    print("\nHome Delivery Charges: ₹50")

    # Add the delivery charge to the final bill
    grand_total = grand_total + 50

# Display the bill
print("\nRice Cost:", rice_cost)
print("Sugar Cost:", sugar_cost)
print("Milk Cost:", milk_cost)
print("-" * 20)
print("Grand Total:", grand_total)
