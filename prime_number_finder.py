def prime_number():
    num = int(input("enter number you want to know is prime: "))
    if num > 0:
        for i in range(2,int(num//2)):
            if num%i == 0:
                print( num ,"is not prime")
                print(num ,"is divided by", i)
                exit(0)
        else:
            print(num, "is prime")
prime_number()