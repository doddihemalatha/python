age=int(input("Enter your Age:"))
medical_certificate=input("Do you have a Medical Certificate Yes/No:").lower()
if age<16:
    print("not Eligible")
elif age>=16 and medical_certificate=="yes":
    print("Membership Approved")
elif age>=16 and medical_certificate=="no":
    print("Bring Medical Certificate")
else:
    print("Invalid")
