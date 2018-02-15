# Computing greatest common divisor using recursion

def gcd(m,n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

m = int(input("Enter first integer: "))
n = int(input("Enter second integer: "))

print("The greatest common divisor is", gcd(m, n))
