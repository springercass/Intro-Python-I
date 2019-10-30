def isPrime(num):
    if int(num) > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print("A number less than or equal to 1 can not be prime")


print("Is your number prime?")
num = input("Enter a number:")
num = int(num)

isPrime(num)
