def isodd(n):
    result = lambda n: n % 2 != 0
    print(result(a))

def isprime(n):
    result = lambda a: a > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
    print(result(n))

def palindrome(n):
    result = lambda a: a == n[::-1]
    print(result(n))


while True:
    print("choose one operation:")
    print("1. isodd")
    print("2. isprime")
    print("3. palindrome")
    print("4. exit")

    choice = input()
    if choice == "1":
        a = int(input("Enter a number:"))
        isodd(a)
    elif choice == "2":
        n = int(input("Enter a number:"))
        isprime(n)
    elif choice == "3":
        n = str(input("Enter a number: "))
        palindrome(n)
    elif choice == "4":
        break
    else:
        print("Invalid input")

