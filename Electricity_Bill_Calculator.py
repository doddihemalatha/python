units=int(input("Enter Units:"))

if units<0:
    print("Invalid Units")
elif units<=100:
    electricity_bill=units*0
    print("Electricity Bill:",electricity_bill)
elif units<=300:
    electricity_bill=units*5
    print("Electricity Bill:",electricity_bill)
else:
    electricity_bill=units*8
    print("Electricity Bill:",electricity_bill)
