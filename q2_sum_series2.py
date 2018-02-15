# Summing series

n = int(input("Enter your integer: "))
m = 0

def sum_series2(i,m):
    if i == 0:
        return m
    else:
        m += i / (2*i + 1)
        return sum_series2(i-1,m)

print(sum_series2(n,m))

