# Summing series

n = int(input("Enter your integer: "))
m = 0

def sum_series1(i,m):
    if i == 0:
        return m
    else:
        m += 1/i
        return sum_series1(i-1,m)

print(sum_series1(n,m))
