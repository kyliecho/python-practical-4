# Finding the number of uppercase letters in a string

def find_num_uppercase(str):
    if len(str) == 0:
        return 0
    else:
        return (str[0].isupper()) + find_num_uppercase(str[1:])

str = str(input("Enter your phrase: "))
print("There are {0} uppercase letter(s) in {1}.".format(find_num_uppercase(str), str))
        
