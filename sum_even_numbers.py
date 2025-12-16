n = int(input("Enter a number: "))

i = 1
sums = 0

while i <= n:
    if i % 2 == 0:
        sums = sums + i
    i += 1

print("Sum of even numbers =", sums)
