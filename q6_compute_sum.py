# Summing the digits in an integer using recursion

n = input("Enter your integer: ")

def sum_digits(n):
    if len(n) == 1:
        return int(n)
    else:
        return int(n[0]) + sum_digits(n[1:])

print("The sum of the digits in", n, "is", sum_digits(n))


    
