# Finding the largest number in an array

def find_largest(alist):
    if len(alist) == 1:
        return alist[0]
    elif alist[0] > find_largest(alist[1:]):
        return alist[0]
    else:
        return find_largest(alist[1:])

A = []
n = int(input("Enter number of integers: "))
for i in range(n):
    num = int(input("Enter integer: "))
    A.append(num)

print("The largest number is", find_largest(A))
