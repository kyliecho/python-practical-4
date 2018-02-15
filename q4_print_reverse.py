# Reverse the digits in an integer recursively

n = input("Enter your integer: ")

def reverse_int(n):
    if len(n) == 1:
        return n
    else:
        return n[-1] + reverse_int(n[:-1])

print("Your integer reversed is", reverse_int(n))


    
