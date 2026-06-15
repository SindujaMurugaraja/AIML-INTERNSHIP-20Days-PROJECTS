# DAY 1 - Factorial & Fibonacci

n = int(input("Enter a number for factorial: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial is:", fact)


X = int(input("Enter number of Fibonacci terms: "))

a, b = 0, 1

print("Fibonacci Series:")
for i in range(X):
    print(a, end=" ")
    a, b = b, a + b
