s=input("enter:")
vowels=0
consonants=0
digits=0
special=0
for i in s:
  if i.isdigit():
    digits=digits+1
  elif i.isalpha():
    if i.lower() in "aeiou":
      vowels+=1
    else:
      consonants+=1
  else:
    special+=1
print("Vowels:", vowels)
print("Consonants:", consonants)
print("digits:", digits)
print("special", special)
