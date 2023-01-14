def factorial(x):
    y = 1
    for i in range(1, x + 1):
        y = y * i
    print("your Factorial is:", y)

n = int(input("Enter your number:"))
factorial(n)
