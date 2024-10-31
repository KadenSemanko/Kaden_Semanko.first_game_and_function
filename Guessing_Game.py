import random as r
num = (r.randint(1,100))
value = 0
while value != num:
    value = int(input("Enter value: "))
    if value > num:
        print("number is too high, try again")
    if value < num:
        print("number is too low, try again")
else:
    print("SWEET SWEET VICTORY")
    exit(0)