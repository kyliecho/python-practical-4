# Occurrences of a specified character in a string

str = input("Enter your word(s): ")
ch = input("Enter target letter: ")

def count_letter(str, ch):
    if ch not in str:
        return 0        
    else:
        return (str[0] == ch) + count_letter(str[1:], ch)
                
print("The letter {0} has appeared {1} time(s) in {2}".format(ch, count_letter(str, ch), str))
